from users.models import User
from django.utils import timezone
from celery import shared_task


@shared_task
def check_user():
    """Checking user's activity. If they don't login throughout the month, they lose status is_active"""
    users = User.objects.all()
    for user in users:
        if user.last_login < timezone.now() - timezone.timedelta(days=30):
            user.is_active = False
            user.save()
