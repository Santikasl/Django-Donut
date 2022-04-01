from django import forms
from .models import *

class RegistrForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'