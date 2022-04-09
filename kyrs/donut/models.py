from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User


class CustomUsers(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=60)
    count_posts = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/', default='static/img/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)




