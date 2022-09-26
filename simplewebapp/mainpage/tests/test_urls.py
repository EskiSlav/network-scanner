from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mainpage.views import index, login_view, logout_view

class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url = resolve(reverse('index'))
        self.assertEquals(url.func, index)

    def test_index_url_is_resolved(self):
        url = resolve(reverse('login'))
        self.assertEquals(url.func, login_view)

    def test_index_url_is_resolved(self):
        url = resolve(reverse('logout'))
        self.assertEquals(url.func, logout_view)
        
    
    
        
        
        