from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription(
            name='Raphael Castro',
            cpf='12345678901',
            email='raphael@castro.net',
            phone='18-93333-3333'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attribute."""
        self.assertIsInstance(self.obj.created_at, datetime)