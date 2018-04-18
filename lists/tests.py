from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolver_to_home_page_view(self):
        found = resolve('/')
        print(found)
        self.assertEqual(found.func, home_page)