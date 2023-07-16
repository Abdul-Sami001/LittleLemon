from django.test import TestCase
from django.urls import reverse
from .models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Burger", price=9.99, inventory=10)
        Menu.objects.create(title="Pizza", price=12.99, inventory=5)

    def test_getall(self):
        
        response = self.client.get(reverse('menu-list'))
        menu_data = response.json()

       
        expected_data = [
            {
                'title': 'Burger',
                'price': 9.99,
                'inventory': 10
            },
            {
                'title': 'Pizza',
                'price': 12.99,
                'inventory': 5
            },
            
        ]

        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(menu_data, expected_data)