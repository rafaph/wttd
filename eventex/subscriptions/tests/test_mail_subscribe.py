from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        self.data = dict(
            name='Raphael Castro',
            cpf='12345678901',
            email='raphael@castro.net',
            phone='11-93333-3333'
        )
        self.client.post('/inscricao/', self.data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self) -> None:
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self) -> None:
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self) -> None:
        expect = ['contato@eventex.com.br', self.data['email']]

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self) -> None:
        for field_name in self.data.keys():
            with self.subTest():
                self.assertIn(self.data[field_name], self.email.body)
