import unittest

from django.test.client import Client

class PostsListViewTest(unittest.TestCase):
    def test_main_page(self):
        client = Client()
        response = client.get('/blog')
        self.assertEquals(response.status_code,200)


