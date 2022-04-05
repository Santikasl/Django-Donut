from django import forms


class AuthForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Логин'}), max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), max_length=60)






