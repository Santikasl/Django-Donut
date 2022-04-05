from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
import re
from django.contrib import messages




def index(request):
    # if request.method == 'POST':
    #     form = RegistrForm(request.POST)
    #     if form.is_valid():
    #         password = form.cleaned_data.get("password")
    #         isPassword = form.cleaned_data.get("password_check")
    #         name = form.cleaned_data.get("name")
    #         if re.match(r'\d', name):
    #             messages.add_message(request, messages.ERROR, 'Логин не должен начинаться с цифры')
    #         elif password != isPassword:
    #             messages.add_message(request, messages.ERROR, 'Пароли не совпадают')
    #         else:
    #             form.save()
    #             return render(request, 'donut/main.html')
    # else:
    #     form = RegistrForm()

    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            name = auth_form.cleaned_data['name']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=name, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вощли в систему')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Пользователь не найден')
            else:
                auth_form.add_error('__all__', 'Ошибка! Пользователь не найден')

        else:
            auth_form = AuthForm()
        context = {
        'form': auth_form
    }
    return render(request, 'donut/index.html', context=context)


def mainl(request):
    return render(request, 'donut/main.html')


def area(request):
    return render(request, 'donut/area.html')



