from django.conf.urls import url, include
from django.views.generic import DateDetailView
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),


    url(r'^main/', views.mainl, name='main'),

]
