from django.forms import model_to_dict
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription.objects.create(
            name='Raphael Castro',
            cpf='12345678901',
            email='raphael@castro.net',
            phone='11-93333-3333'
        )
        self.res = self.client.get(f'/inscricao/{self.obj.pk}/')

    def test_get(self):
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.res,
            'subscriptions/subscription_detail.html'
        )

    def test_context(self):
        subscription = self.res.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = model_to_dict(self.obj, exclude=['id']).values()
        with self.subTest():
            for expected in contents:
                self.assertContains(self.res, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        res = self.client.get('/inscricao/0/')
        self.assertEqual(404, res.status_code)
