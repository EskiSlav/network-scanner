from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cabinet.views import cabinet, send_messages

class TestUrls(SimpleTestCase):
    
    def test_cabinet_resolves(self):
        url = resolve(reverse('cabinet'))
        self.assertEquals(url.func, cabinet)

    def test_messages_resolves(self):
        url = resolve(reverse('messages', args=['123456789']))
        self.assertEquals(url.func, send_messages)
                
        