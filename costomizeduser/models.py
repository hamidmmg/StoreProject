from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Phone = models.CharField(max_length=15, default=None, blank=True, null=True)
    profile_image = models.ImageField(upload_to='files/profiles', blank=True)
    email = models.EmailField(unique=True, blank=True)




