from django.core.management import BaseCommand
import datetime

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        user1 = User.objects.create(email='test@test.ru', phone='+79999999999')
        user1.save()
        user2 = User.objects.create(email='second@second.ru', phone='+78888888888')
        user2.save()

        course1 = Course.objects.create(title='Django', description='haha')
        course1.save()
        course2 = Course.objects.create(title='DRF', description='hehe')
        course2.save()

        lesson1 = Lesson.objects.create(title='Generics', description='lala', course=course1)
        lesson1.save()
        lesson2 = Lesson.objects.create(title='Patterns', description='blabla', course=course1)
        lesson2.save()
        lesson3 = Lesson.objects.create(title='Postman', description='lele', course=course2)
        lesson3.save()

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
            paid_lesson=lesson2,
            value=25000,
            pay_method='Cash'
        )
        payment2.save()
