from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .forms import *
from .forms import Imgform
from django.contrib import messages

from .models import CustomUsers


def reg(request):
    if request.user.is_authenticated == True:
        return render(request, 'donut/main.html', {'post': NewPosts})
    else:
        if request.method == 'POST':
            form = ExtendedRegisterForm(request.POST)

            if form.is_valid():
                cUser = CustomUsers()
                cUser.name = request.POST.get("username")
                cUser.email = request.POST.get("email")
                cUser.password = request.POST.get("password1")
                cUser.user = form.save()

                cUser.save()

                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'donut/main.html', {'post': NewPosts})
        else:
            form = ExtendedRegisterForm()
        return render(request, 'donut/reg.html', {'form': form, 'post': NewPosts})


def mainl(request):
    pos = Posts.objects.all()
    auth_form = AuthForm()
    if request.user.is_authenticated == False:
        return render(request, 'donut/index.html', {'form': auth_form, 'post': NewPosts, 'pos': pos})
    else:
        return render(request, 'donut/main.html', {'post': NewPosts, 'pos': pos})


def index(request):
    if request.user.is_authenticated == True:
        return render(request, 'donut/main.html', {'post': NewPosts})
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
                        return render(request, 'donut/main.html', {'post': NewPosts})
                    else:
                        messages.add_message(request, messages.ERROR, 'Пользователь больше не активен')
                        return render(request, 'donut/index.html', {'form': auth_form, 'post': NewPosts})
                else:
                    messages.add_message(request, messages.ERROR, 'Проверьте правильность введённых данных')
                    return render(request, 'donut/index.html', {'form': auth_form, 'post': NewPosts})
            else:
                auth_form = AuthForm()
                return render(request, 'donut/index.html', {'form': auth_form, 'post': NewPosts})
        else:
            auth_form = AuthForm()
            context = {

                'form': auth_form,
                'post': NewPosts
            }
            return render(request, 'donut/index.html', context=context)


def area(request):
    auth_form = AuthForm()

    if request.user.is_authenticated == False:
        return render(request, 'donut/index.html', {'form': auth_form, 'post': NewPosts})
    else:
        cUser = CustomUsers.objects.get(user=request.user)
        postt = Posts(user=request.user)
        ppp = Posts.objects.filter(user=request.user)
        if request.method == 'POST':
            imgForm = Imgform(request.POST, request.FILES)
            newPost = NewPosts(request.POST, request.FILES)
            if newPost.is_valid():
                postt.img = newPost.cleaned_data['postImg']
                postt.description = newPost.cleaned_data['description']
                postt.save()
                return HttpResponseRedirect(reverse('area'))
            if imgForm.is_valid():

                if imgForm.cleaned_data['img'] is not None:
                    cUser.img = imgForm.cleaned_data['img']
                    cUser.save()
                    return render(request, 'donut/area.html',
                                  {'form': imgForm, 'cUser': cUser, 'post': NewPosts, 'ppp': ppp})
        else:
            imgForm = Imgform()

        return render(request, 'donut/area.html', {'form': imgForm, 'cUser': cUser, 'post': NewPosts, 'ppp': ppp})


def search(request):
    pass


def search_results(request):
    if request.is_ajax():
        res = None
        dataName = request.POST.get('dataName')
        qs = CustomUsers.objects.filter(name__icontains=dataName)
        print(qs)
        if len(qs) > 0 and len(dataName) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'name': pos.name,
                    'img': str(pos.img.url)
                }
                data.append(item)
            res = data
        else:
            res = 'Пользователь не найден'
        return JsonResponse({'data': res})
    return JsonResponse({})
