from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User


class CustomUsers(models.Model):
    name = models.CharField(max_length=100, default='none')
    count_posts = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/', default='images/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




