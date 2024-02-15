from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.CharField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='phone')
    city = models.CharField(max_length=20, **NULLABLE, verbose_name='city')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='image')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
