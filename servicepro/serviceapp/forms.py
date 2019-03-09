from django import forms
from .models import Vehicle, Appointment, AppointmentDetail, CarService
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email', 'password']