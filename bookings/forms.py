from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    """Form for customers to make a reservation. Separates form logic from views, making views easier to read and maintain"""
    class Meta:
        model = Reservation  # Link the form to the Reservation model
        fields = ['name', 'email', 'phone', 'table', 'date', 'time', 'guests']  # Fields to include in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Use date picker for the date field
            'time': forms.TimeInput(attrs={'type': 'time'}),  # Use time picker for the time field
        }