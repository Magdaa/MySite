import os
import unittest
from datetime import timezone
from unittest import mock
from blog import models

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
        self.assertTrue('post_list' in response.context)

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


class PostListIndexViewTest2(TestCase):
    def setUp(self):
        self.factory = RequestFactory

        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.post = Post.objects.create()



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



class PostByCategoryTest(unittest.TestCase):
    def test_filter_by_category(self):
        category = mock.Mock()
        post = mock.Mock(spec=models.PostManager)
        models.PostManager.filter_by_category(post,category)
        post.filter.assert_called_with(category=category)

    @mock.patch('blog.models.PostManager.filter', mock.Mock())
    def test_filters_by_category_with_patch(self):
        category = mock.Mock()
        models.Post.objects.filter_by_category(category)
        models.Post.objects.filter.assert_called_with(category=category)

    @mock.patch('blog.models.PostManager.filter')
    def test_filters_by_category_with_patch_and_filter_passed_in(self, filter_method):
        category = mock.Mock()
        models.Post.objects.filter_by_category(category)
        filter_method.assert_called_with(category=category)