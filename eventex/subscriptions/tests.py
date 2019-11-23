from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTestCase(TestCase):
    def setUp(self) -> None:
        self.res = self.client.get('/inscricao/')

    def test_get(self) -> None:
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self) -> None:
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.res, 'subscriptions/subscription_form.html')

    def test_html(self) -> None:
        """Html must contain input tags"""
        self.assertContains(self.res, '<form')
        self.assertContains(self.res, '<input', 6)
        self.assertContains(self.res, 'type="text"', 3)
        self.assertContains(self.res, 'type="email"')
        self.assertContains(self.res, 'type="submit"')

    def test_csrf(self) -> None:
        """Html must contain csrf"""
        self.assertContains(self.res, 'csrfmiddlewaretoken')

    def test_has_form(self) -> None:
        """Context must have subscription form"""
        form = self.res.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self) -> None:
        """Form must have 4 fields"""
        form = self.res.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostTestCase(TestCase):
    def setUp(self) -> None:
        self.data = dict(
            name='Raphael Castro',
            cpf='12345678901',
            email='raphael@castro.net',
            phone='11-93333-3333'
        )
        self.res = self.client.post('/inscricao/', self.data)

    def test_post(self) -> None:
        """Valid POST should redirect to /inscricao/"""

        self.assertEqual(302, self.res.status_code)

    def test_send_subscribe_email(self) -> None:
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self) -> None:
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self) -> None:
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self) -> None:
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', self.data['email']]

        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self) -> None:
        email = mail.outbox[0]
        self.assertIn(self.data['name'], email.body)
        self.assertIn(self.data['cpf'], email.body)
        self.assertIn(self.data['email'], email.body)
        self.assertIn(self.data['phone'], email.body)


class SubscribeInvalidPostTestCase(TestCase):
    def setUp(self) -> None:
        self.res = self.client.post('/inscricao/', {})

    def test_post(self) -> None:
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.res, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.res.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.res.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessageTestCaste(TestCase):
    def test_message(self):
        data = dict(
            name='Raphael Castro',
            cpf='12345678901',
            email='raphael@castro.net',
            phone='19-93333-3333'
        )
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')
