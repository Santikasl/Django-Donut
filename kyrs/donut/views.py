from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'donut/index.html')


def mainl(request):
    return render(request, 'donut/main.html')

