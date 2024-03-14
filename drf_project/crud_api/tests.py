from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item


class ItemAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)  # Authenticate the test client with the test user

    def test_create_item(self):
        data = {
            "name": "Test Item",
            "category": "Test Category",
            "subcategory": "Test Subcategory",
            "amount": 10
        }

        response = self.client.post('/items/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Item.objects.filter(name=data['name']).exists())

