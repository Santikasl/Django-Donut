from django.conf.urls import url
from django.contrib.auth import views as authViews

from django.urls import path, reverse
from . import views

urlpatterns = [

    path('', views.signIn, name='signIn'),
    path('reg/', views.reg, name='reg'),
    path('main/', views.mainl, name='main'),
    path('area/', views.area, name='area'),
    path('like/', views.like, name='like'),
    path('search/', views.search_results, name='search'),
    path('siwtch_follow/', views.follow_unfollow, name='follow-unfollow-view'),
    path('sort/', views.sort, name='sort'),
    path('statistics/', views.statistics, name='statistics'),
    path('edit/', views.edit, name='edit'),
    path('like/', views.like, name='like'),
    path('delite', views.delite, name='delite'),
    path('<int:pk>/', views.search_profile, name='profile'),
    path('exit/', views.logout_user, name='exit'),


]


