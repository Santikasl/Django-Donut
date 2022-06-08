from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .forms import *
from .forms import Imgform
from django.contrib import messages
from .models import CustomUsers



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('reg'))


def reg(request):
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(reverse('main'))
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
    if request.user.is_authenticated == False:
        return render(request, 'donut/index.html')
    else:
        postt = Posts(user=request.user)
        cUser = CustomUsers.objects.get(user=request.user)
        pos = Posts.objects.all()
        newPost = NewPosts(request.POST, request.FILES)
        if newPost.is_valid():
            postt.img = newPost.cleaned_data['postImg']
            postt.description = newPost.cleaned_data['description']
            postt.save()
            return HttpResponseRedirect(reverse('area'))
        return render(request, 'donut/main.html', {'post': NewPosts, 'pos': pos, 'cUser': cUser, 'post': NewPosts})


def signIn(request):
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(reverse('main'))
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
                        return HttpResponseRedirect(reverse('main'))
                    else:
                        messages.add_message(request, messages.ERROR, 'Пользователь больше не активен')
                        return render(request, 'donut/index.html',
                                      {'form': auth_form})
                else:
                    messages.add_message(request, messages.ERROR, 'Проверьте правильность введённых данных')
                    return render(request, 'donut/index.html',
                                  {'form': auth_form})
            else:
                auth_form = AuthForm()
                return render(request, 'donut/index.html',
                              {'form': auth_form})
        else:
            auth_form = AuthForm()
            context = {
                'form': auth_form,
                'post': NewPosts,
            }
            return render(request, 'donut/index.html', context=context)


def area(request):
    auth_form = AuthForm()

    if request.user.is_authenticated == False:
        return render(request, 'donut/index.html', {'form': auth_form})
    else:
        cUser = CustomUsers.objects.get(user=request.user)
        postt = Posts(user=request.user)
        all_post_user = Posts.objects.filter(user=request.user)
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
                                  {'form': imgForm, 'cUser': cUser, 'post': NewPosts, 'all_post_user': all_post_user})
        else:
            imgForm = Imgform()

        return render(request, 'donut/area.html',
                      {'form': imgForm, 'cUser': cUser, 'post': NewPosts, 'all_post_user': all_post_user})


def search_profile(request, pk):
    search_user = CustomUsers.objects.filter(pk=pk).first()
    # print(search_user)
    all_post_user = Posts.objects.filter(user=search_user.user)
    print(all_post_user)
    obj = CustomUsers.objects.filter(pk=pk).first
    if obj:
        return render(request, 'donut/profile.html',
                      {'obj': obj, 'pk': pk, 'post': NewPosts, 'all_post_user': all_post_user})


def search_results(request):
    if request.is_ajax():
        res = None
        dataName = request.POST.get('dataName')
        # фильтр работает правильно я проверил
        qs = CustomUsers.objects.filter(name__icontains=dataName)[:4]
        if len(qs) > 0 and len(dataName) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'name': pos.name,
                    'count_posts': pos.count_posts,
                    'likes': pos.likes,
                    'followers': pos.followers,
                    'img': pos.img.url,
                }

                data.append(item)

            res = data
        else:
            res = 'Пользователь не найден'
        return JsonResponse({'data': res})
    return JsonResponse({})


def sort(request):
    if request.is_ajax():
        all_post = Posts.objects.order_by('-date')
        data = []
        for pos in all_post:
            item = {
                'pk': pos.pk,
                'descriptions': pos.description,
                'img': pos.img.url,
            }
            data.append(item)
        res_post = data
        return JsonResponse({'data': res_post})
    return JsonResponse({})


def delite(request):
    if request.method == 'POST':
        post_id = request.POST['id']
        print(post_id)
        post = Posts.objects.get(id=post_id)
        post.delete()
    return HttpResponseRedirect(reverse('area'))


def edit(request):
    if request.is_ajax():
        id = request.POST.get('id', None)
        post2 = Posts.objects.get(id=id)
        post2.description = request.POST.get('description', None)
        post2.save()
        data2 = post2.description
        # for posi in post:
        #     item = {
        #         'pk': posi.pk,
        #         'descriptions': posi.description,
        #         'img': posi.img.url,
        #     }
        #     data2.append(item)
        res_post2 = data2
        return JsonResponse({'data': res_post2})




