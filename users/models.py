from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.CharField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='phone')
    city = models.CharField(max_length=20, **NULLABLE, verbose_name='city')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='image')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Payment(models.Model):
    PAY_METHOD = [
        ('Cash', 'Cash'),
        ('Transfer to card', 'Transfer to card')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    pay_date = models.DateField(**NULLABLE, verbose_name='pay_date')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='paid_course', **NULLABLE)
    value = models.IntegerField(verbose_name='value', default=30000)
    pay_method = models.CharField(choices=PAY_METHOD, verbose_name='pay_method')
    payment_link = models.URLField(max_length=500, verbose_name='payment_link', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='payment_id', **NULLABLE)
    status = models.CharField(verbose_name='status', **NULLABLE)

    def __str__(self):
        return f"{self.payment_id}"

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
