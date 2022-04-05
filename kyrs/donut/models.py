from django.db import models
from django.core.validators import *

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    img = models.ImageField()
    password = models.CharField(max_length=60)


