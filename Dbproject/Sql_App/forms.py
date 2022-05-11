from django.core import validators
from django import forms #building function in djagno
from .models import User # import object form Models.py

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email','password' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }# for goodlooking forms

