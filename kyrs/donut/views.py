from django.shortcuts import render
from django.http import HttpResponse

from .forms import *


def index(request):
    form = RegistrForm()
    return render(request, 'donut/index.html', {'form': form})


def mainl(request):
    return render(request, 'donut/main.html')

def area(request):
    return render(request, 'donut/area.html')



