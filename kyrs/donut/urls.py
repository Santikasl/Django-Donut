
from django.contrib.auth import views as authViews

from django.urls import path, reverse
from . import views
urlpatterns = [

    path('', views.index, name='index'),

    path('reg/', views.reg, name='reg'),

    path('main/', views.mainl, name='main'),

    path('area/', views.area, name='area'),

    path('exit/', authViews.LogoutView.as_view(), name='exit'),

]