from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson


class CourseTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='test',
            description='test'
        )

    def test_get_course(self):
        response = self.client.get('education:course')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonTestCase(APITestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(
            name='test1',
            description='test1'
        )

    def test_get_lesson(self):
        response = self.client.get('education:lesson-list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)