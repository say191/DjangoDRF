from django.core.management import BaseCommand
import datetime

from materials.models import Course, Lesson
from users.models import Payment, User
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Group.objects.all().delete()
        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        group = Group(name='Moderators')
        group.save()

        user = User.objects.create(email='admin', is_superuser=True, is_staff=True)
        user.set_password('111')
        user.save()
        user1 = User.objects.create(email='zero@zero.ru', phone='+71111111111')
        user1.set_password('000')
        user1.save()
        user2 = User.objects.create(email='second@second.ru', phone='+72222222222')
        user2.set_password('222')
        user2.save()
        user3 = User.objects.create(email='third@third.ru', phone='+73333333333')
        user3.set_password('333')
        user3.groups.add(group)
        user3.save()
        user4 = User.objects.create(email='forth@forth.ru', phone='+74444444444')
        user4.set_password('444')
        user4.groups.add(group)
        user4.save()

        course1 = Course.objects.create(title='Django', description='haha')
        course1.save()
        course2 = Course.objects.create(title='DRF', description='hehe')
        course2.save()

        lesson1 = Lesson.objects.create(title='Generics', description='lala', course=course1, owner=user1)
        lesson1.save()
        lesson2 = Lesson.objects.create(title='Patterns', description='blabla', course=course1, owner=user1)
        lesson2.save()
        lesson3 = Lesson.objects.create(title='Postman', description='lele', course=course2, owner=user2)
        lesson3.save()
        lesson4 = Lesson.objects.create(title='Test', description='test', course=course2, owner=user2)
        lesson4.save()

        payment1 = Payment.objects.create(
            user=user1,
            pay_date=datetime.datetime.now().date(),
            paid_course=course1,
            value=100000,
            pay_method='Transfer to card'
        )
        payment1.save()
        payment2 = Payment.objects.create(
            user=user2,
            pay_date=datetime.datetime.now().date(),
            paid_course=course2,
            value=25000,
            pay_method='Cash'
        )
        payment2.save()
