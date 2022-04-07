from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User



# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=60)


class Profile(models.Model):
    img = models.ImageField(upload_to='profile_pics', blank=True)
    followers = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
