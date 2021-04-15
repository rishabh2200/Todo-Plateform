from django.test import TestCase, Client
from django.urls import reverse
import json

from rest_framework import status
from rest_framework.test import APITestCase

from todo.serializers import TodoSerializer
from todo.models import Todo


class AddTaskTest(APITestCase):
    ''' testing class in django '''

    def test_registration(self):
        data = {'title': ['title for testing'],
                'reminder_datatime': ['2021-02-09 12:51'],
                'description': ['description for testing'],
                'completed': ['True']}
        test_url = reverse('addTask')
        response = self.client.post(test_url, data) 
        data1=Todo.objects.get(pk=response.data['id'])
        self.assertEqual(str(data1), 'title for testing')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


