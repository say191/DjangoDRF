from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru",
            is_active=True
        )
        self.user.set_password("111")
        self.user.save()

        self.course = Course.objects.create(
            title="Test",
            description="Test",
            owner=self.user
        )
        self.course.save()

        self.lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson',
            course=self.course,
            owner=self.user
        )
        self.lesson.save()

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        """Testing list of lessons"""
        response = self.client.get(
            reverse('materials:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None, 'results': [
                {'id': 1, 'course': 'Test', 'title': 'Test_lesson', 'description': 'Test_lesson', 'preview': None,
                 'video_url': None, 'owner': 1}]}

        )

    def test_create_lesson(self):
        """Testing to create lesson"""

        data = {
            "title": "Test_lesson_new",
            "description": "Test_lesson_new",
            "course": self.course,
            "owner": self.user
        }

        response = self.client.post(
            'lessons/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json()['title'],
            data['title']
        )

    def test_update_lesson(self):
        """Testing to change lesson"""
        lesson = Lesson.objects.create(
            title='Test_lesson_new_2',
            description='Test_lesson_new_2',
            course=self.course,
            owner=self.user
        )
        lesson.save()

        response = self.client.patch(
            f'/lessons/update/{lesson.id}',
            {'description': 'new_description'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Testing to delete lesson"""
        lesson = Lesson.objects.create(
            title='Test_lesson_new_3',
            description='Test_lesson_new_3',
            course=self.course,
            owner=self.user
        )
        lesson.save()

        response = self.client.delete(
            f'/lessons/delete/{lesson.id}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru",
            is_active=True
        )
        self.user.set_password("111")
        self.user.save()

        self.course = Course.objects.create(
            title="Test_course",
            description="Test_course",
            owner=self.user
        )
        self.course.save()

        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        """Testing to subscribe on course"""

        data = {
            "user": self.user.id,
            "course": self.course.id,
        }

        response = self.client.post(
            reverse('materials:subscribe'),
            data=data
        )
        print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'You have subscribed'}
        )
