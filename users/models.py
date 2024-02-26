from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.CharField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='phone')
    city = models.CharField(max_length=20, **NULLABLE, verbose_name='city')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='image')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    PAY_METHOD = [
        ('Cash', 'Cash'),
        ('Transfer to card', 'Transfer to card')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    pay_date = models.DateField(**NULLABLE, verbose_name='pay_date')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='paid_course', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='paid_lesson', **NULLABLE)
    value = models.IntegerField(**NULLABLE, verbose_name='value')
    pay_method = models.CharField(choices=PAY_METHOD, verbose_name='pay_method')