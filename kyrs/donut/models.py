from datetime import datetime

from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from PIL import Image

MALE_CHOICES = (
    ('female', 'FEMALE'),
    ('male', 'MALE'),
)


class CustomUsers(models.Model):
    name = models.CharField(max_length=100, default='none')
    count_posts = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    img = models.ImageField(upload_to='images/', default='images/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    male = models.CharField(max_length=6, choices=MALE_CHOICES, default='male')

    def __str__(self):
        return str(self.name)


def default_datetime():
    return datetime.now()


class Posts(models.Model):
    description = models.TextField(max_length=2000)
    date = models.DateTimeField(default=default_datetime)
    user = models.ForeignKey(CustomUsers, null=True, blank=True, on_delete=models.CASCADE, related_name='creaters')
    img = models.ImageField(upload_to='posts/')
    liked = models.ManyToManyField(User, default=None, blank=True)

    @property
    def num_likes(self):
        return self.liked.all().count()

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.img.path)

        if img.height > 900 or img.width > 900:
            output_size = (720, 900)
            img.thumbnail(output_size)
            img.save(self.img.path)


LIKE_CHOICES = {
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
}


class LikesPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return f' {self.user}: {self.post.id}'


class Facts(models.Model):
    description = models.TextField(max_length=2000)




