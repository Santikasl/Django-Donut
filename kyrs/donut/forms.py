from django import forms
from django.core.exceptions import ValidationError
import re
from .models import *
from django.contrib import messages


class RegistrForm(forms.ModelForm):
    password_check = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Users
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Электронный адрес'}),

        }





