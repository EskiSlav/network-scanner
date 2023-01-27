from django.test import TestCase, Client
from django.urls import reverse
from cabinet.models import Messages, Users


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        user = Users.objects.create(
            tg_id=123456789,
            username="eskislav",
            first_name="Viacheslav",
            last_name="Kozachok",
            is_bot=False
        )
        message = Messages.objects.create(
            message_id=12345642,
            user=user,
            text="Some Text",
            direction="to"
        )

        user.save()
        message.save()


    def test_get_messages_for_user_not_AJAX(self):
        """Check response without """
        
        url = reverse('messages', args=[123456789])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 400)
    
    def test_get_messages_for_user_AJAX(self):
        """Check response with AJAX Header """
        
        url = reverse('messages', args=[123456789])
        headers = {"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"}
        response = self.client.get(url, **headers)

        expected_response_text = {"0":[{
                    'user_id': 123456789, 
                    'text': 'Some Text', 
                    'direction': 'to', 
                    'message_id': 12345642
                }
            ]
        }

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), expected_response_text)

    def test_cabinet_redirect_non_logged_user_from_cabinet(self):
        response = self.client.get(reverse('cabinet'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

