from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        

    def test_get_messages_for_user(self):
        url = reverse('messages', args=[123456789])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)