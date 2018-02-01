import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MySite.settings")
import django
django.setup()
import factory
from django.test import TestCase, RequestFactory

from blog.models import Post, Comment
from blog.views import PostsList, index
from blog.forms import CommentForm




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


class PostFactory(factory.Factory):
    class Meta:
        model = Post
    slug = "test-slug"

class CommentFactory(factory.Factory):
    class Comment:
        model = Comment
    author = 'magda'

    post = factory.SubFactory(PostFactory)

class CommentViewTest(TestCase):
    def test_valid_data(self):
        form = CommentForm()
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.author,'magda')


