from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTestCase(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(r('home'))

    def test_get(self) -> None:
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self) -> None:
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = f'href="{r("subscriptions:new")}"'
        self.assertContains(self.response, expected)
