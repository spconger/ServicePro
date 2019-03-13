from django import forms
from .models import Vehicle, Appointment, AppointmentDetail, CarService
from django.contrib.auth.models import User

#user form from auth. Not a good idea to display all the fields
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email', 'password']

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields='__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

class AppointmentDetailForm(forms.ModelForm):
    class Meta:
        model=AppointmentDetail
        fields='__all__'