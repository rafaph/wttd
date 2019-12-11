from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTestCase(TestCase):
    fixtures = ['keynotes.json']

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

    def test_speakers(self):
        """Must show keynotes speakers"""
        contents = [
            f'href="{r("speaker_detail", slug="grace-hopper")}"',
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            f'href="{r("speaker_detail", slug="alan-turing")}"',
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = f'href="{r("home")}#speakers"'
        self.assertContains(self.response, expected)
