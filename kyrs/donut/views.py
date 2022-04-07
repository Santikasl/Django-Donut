

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
import re
from django.contrib import messages


def reg(request):
    if request.user.is_authenticated == True:
            return render(request, 'donut/main.html')
    else:
        if request.method == 'POST':
            form = ExtendedRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'donut/main.html')
        else:
            form = ExtendedRegisterForm()
        return render(request, 'donut/reg.html', {'form': form})


def mainl(request):
    auth_form = AuthForm()
    if request.user.is_authenticated == False:
            return render(request, 'donut/index.html', {'form': auth_form})
    else:
        return render(request, 'donut/main.html')


def index(request):
    if request.user.is_authenticated == True:
            return render(request, 'donut/main.html')
    else:
        if request.method == 'POST':
            auth_form = AuthForm(request.POST)
            if auth_form.is_valid():
                name = auth_form.cleaned_data['name']
                password = auth_form.cleaned_data['password']
                user = authenticate(username=name, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        return render(request, 'donut/main.html')
                    else:
                        messages.add_message(request, messages.ERROR, 'Пользователь больше не активен')
                        return render(request, 'donut/index.html', {'form': auth_form})
                else:
                    messages.add_message(request, messages.ERROR, 'Проверьте правильность введённых данных')
                    return render(request, 'donut/index.html', {'form': auth_form})
            else:
                auth_form = AuthForm()
                return render(request, 'donut/index.html', {'form': auth_form})
        else:
            auth_form = AuthForm()
            context = {

                'form': auth_form
            }
            return render(request, 'donut/index.html', context=context)


def area(request):
    auth_form = AuthForm()
    if request.user.is_authenticated == False:
            return render(request, 'donut/index.html', {'form': auth_form})
    else:
        return render(request, 'donut/area.html')



