from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self) -> None:
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='ABCD1234567')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits."""
        form = self.make_validated_form(cpf='12345')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name='RAPHAEL castro')
        self.assertEqual('Raphael Castro', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional."""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional."""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_invalid_email_and_optional_phone(self):
        """Invalid email and optional phone must have errors"""
        # tip: this occurs because the key "email" is exclusively on errors or cleaned_data
        form = self.make_validated_form(email="invalidemail")
        self.assertTrue(form.errors)

    def test_must_informe_email_or_phone(self):
        """Email and Phone are optional, but one must be informed."""
        form = self.make_validated_form(phone="", email="")
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(
            name='Raphael Castro',
            cpf='12345678901',
            email='raphael@castro.net',
            phone='21-996866180'
        )
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
