from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=30, verbose_name='title')
    preview = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='preview')
    description = models.TextField(max_length=100, verbose_name='description')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='owner')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    title = models.CharField(max_length=30, verbose_name='title')
    description = models.TextField(max_length=100, verbose_name='description')
    preview = models.ImageField(upload_to='lessons/', **NULLABLE, verbose_name='preview')
    video_url = models.URLField(**NULLABLE, verbose_name='video_url')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='description')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='owner')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='user')
    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE, **NULLABLE, verbose_name='course')
    sub_status = models.BooleanField(default=False, verbose_name='sub_status', **NULLABLE)

    def __str__(self):
        return f'{self.user}, {self.course}, {self.sub_status}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
