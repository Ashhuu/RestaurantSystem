from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# Create your models here.


class UserDetails(AbstractUser):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=120)
    email = models.EmailField(max_length=50)
    details = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()