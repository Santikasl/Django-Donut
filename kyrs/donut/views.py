from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import re
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            isPassword = form.cleaned_data.get("password_check")
            name = form.cleaned_data.get("name")
            if re.match(r'\d', name):
                messages.add_message(request, messages.ERROR, 'Логин не должен начинаться с цифры')
            elif password != isPassword:
                messages.add_message(request, messages.ERROR, 'Пароли не совпадают')
            else:
                form.save()
                return render(request, 'donut/main.html')
    else:
        form = RegistrForm()
    return render(request, 'donut/index.html', {'form': form})


def mainl(request):
    return render(request, 'donut/main.html')


def area(request):
    return render(request, 'donut/area.html')



