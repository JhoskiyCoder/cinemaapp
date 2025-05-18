from django import forms
from .models import Viewer, Ticket

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    phone = forms.CharField(max_length=20, label='Телефон')
    email = forms.EmailField(label='Email')
    seat_number = forms.CharField(widget=forms.HiddenInput())
