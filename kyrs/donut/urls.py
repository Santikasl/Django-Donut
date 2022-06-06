from django.conf.urls import url
from django.contrib.auth import views as authViews

from django.urls import path, reverse
from . import views

urlpatterns = [

    path('', views.signIn, name='signIn'),
    path('reg/', views.reg, name='reg'),
    path('main/', views.mainl, name='main'),
    path('area/', views.area, name='area'),
    path('search/', views.search_results, name='search'),
    path('sort/', views.sort, name='sort'),

    path('<int:pk>/', views.search_profile, name='profile'),
    path('exit/', views.logout_user, name='exit'),

]
