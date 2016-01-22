from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form deve ter 4 campos"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))
