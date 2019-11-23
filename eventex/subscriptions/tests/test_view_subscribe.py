from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
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
        tags = [
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1)
        ]
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.res, text, count)

    def test_csrf(self) -> None:
        """Html must contain csrf"""
        self.assertContains(self.res, 'csrfmiddlewaretoken')

    def test_has_form(self) -> None:
        """Context must have subscription form"""
        form = self.res.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
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


class SubscribePostInvalid(TestCase):
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


class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(
            name='Raphael Castro',
            cpf='12345678901',
            email='raphael@castro.net',
            phone='19-93333-3333'
        )
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')