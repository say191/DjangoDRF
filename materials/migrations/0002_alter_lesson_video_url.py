# Generated by Django 5.0.2 on 2024-02-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='video_url'),
        ),
    ]