from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self) -> None:
        self.speaker = Speaker.objects.create(
            name='Raphael Castro',
            slug='raphael-castro',
            photo='http://rcn.link/rc-pic'
        )

    def test_email(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='raphael@castro.net',
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='11-91111-1111',
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(
            speaker=self.speaker,
            kind='A',
            value='B'
        )
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='raphael@castro.net',
        )
        self.assertEqual('raphael@castro.net', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self) -> None:
        s = Speaker.objects.create(
            name='Raphael Castro',
            slug='raphael-castro',
            photo='http://hbn.link/hb-pic'
        )
        s.contact_set.create(kind=Contact.EMAIL, value='raphael@castro.net')
        s.contact_set.create(kind=Contact.PHONE, value='19-999999999')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['raphael@castro.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['19-999999999']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
