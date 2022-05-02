from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CustomUsers, Posts


class AuthForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Логин'}), max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), max_length=60)


class NewPosts(forms.ModelForm):
    postImg = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'input-file', 'id': 'file','type':'file', 'name': 'file','accept':'image/jpeg, image/png'}))
    description = forms.Textarea()

    class Meta:
        model = Posts
        fields = ['postImg', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Описание', 'maxlength': '2000'}),
        }


class ExtendedRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), max_length=60)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}), max_length=60)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Логин'}), max_length=60)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Imgform(forms.ModelForm):
    img = forms.ImageField(required=False, widget=forms.FileInput(attrs={'onchange': 'this.form.submit()'}))

    class Meta:
        model = CustomUsers
        fields = ['img']




























