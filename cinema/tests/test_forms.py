from django.test import TestCase
from cinema.forms import BookingForm, SignUpForm


class FormTests(TestCase):
    def test_booking_form_valid(self):
        form = BookingForm(data={"seats_booked": 2})
        self.assertTrue(form.is_valid(), form.errors)

    def test_booking_form_invalid_zero(self):
        form = BookingForm(data={"seats_booked": 0})
        self.assertFalse(form.is_valid())

    def test_signup_form_fields_present(self):
        form = SignUpForm()
        for name in ["username", "password1", "password2"]:
            self.assertIn(name, form.fields)
