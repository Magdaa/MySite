from django.test import TestCase, RequestFactory

from blog.models import Post
from blog.views import PostsList, index,current_datetime



class PostsListViewTest(TestCase):
    def test_main_page(self):
        response = self.client.get('/blog')
        self.assertEquals(response.status_code,200)
        #self.assertTrue('posts_list' in response.context)

    def setUp(self):
        self.factory = RequestFactory()

    def test_main_page_reguestFactory(self):
        request = self.factory.get('/fake_path')
        view = PostsList.as_view(template_name='fake.html')
        response = view(request)
        self.assertEquals(response.status_code,200)
        self.assertEqual(response.template_name[0], 'fake.html')

class IndexViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_page_requestFactory(self):
        request = self.factory.get('/fake_path')
        response = index(request)
        self.assertEquals(response.status_code, 200)

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

