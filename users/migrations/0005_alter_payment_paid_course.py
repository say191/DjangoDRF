# Generated by Django 4.2.7 on 2024-02-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_lesson_video_url'),
        ('users', '0004_remove_payment_paid_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_course',
            field=models.ManyToManyField(to='materials.course', verbose_name='paid_course'),
        ),
    ]