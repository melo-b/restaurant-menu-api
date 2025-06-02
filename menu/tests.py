from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category, MenuItem
from django.contrib.auth.models import User

# Create your tests here.
class MenuItemTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.category = Category.objects.create(name='Main Course')
        self.item = MenuItem.objects.create(
            name='Pasta',
            description='Creamy Alfredo',
            price=12.99,
            available=True,
            category=self.category
        )

    def test_get_menu_items(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_menu_item_unauthorized(self):
        response = self.client.post('/api/menu-items/', {
            'name': 'Pizza',
            'description': 'Cheese',
            'price': 9.99,
            'available': True,
            'category_id': self.category.id
        })
        self.assertEqual(response.status_code, 401)

    def test_create_menu_item_authorized(self):
        self.client.login(username='testuser', password='pass1234')
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/menu-items/', {
            'name': 'Pizza',
            'description': 'Cheese',
            'price': 9.99,
            'available': True,
            'category_id': self.category.id
        })
        self.assertEqual(response.status_code, 201)