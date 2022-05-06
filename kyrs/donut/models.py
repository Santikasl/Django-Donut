from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from PIL import Image

class CustomUsers(models.Model):
    name = models.CharField(max_length=100, default='none')
    count_posts = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/', default='images/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Posts(models.Model):
    description = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='posts/')

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.img.path)

        if img.height > 900 or img.width > 900:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.img.path)






