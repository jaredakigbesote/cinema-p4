from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seats']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

