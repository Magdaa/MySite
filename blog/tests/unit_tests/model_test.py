from datetime import timezone
from unittest import TestCase, mock
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MySite.settings")

import django
django.setup()
from model_mommy import mommy
from blog.models import Post, Category
import factory



class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post(title='Fake title')
        self.assertEqual(str(post), post.title)



class CategoryTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="LastCategory")


    def test_categories_count(self):
        lastCategory = Category.objects.filter().last()
        self.assertEqual(str(lastCategory), 'LastCategory')



class PostModelFixtureTest(TestCase):
    fixtures = ['blog/fixtures/post.json']

    def test_post_creation(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title,'Just test')


class PostModelMommyTest(TestCase):
    def test_post_creation(self):
        post=mommy.make(Post, title = 'Just test')
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.title,'Just test')

class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    name = 'testcategory'

class PostFactory(factory.Factory):
    class Meta:
        model = Post

    category = factory.SubFactory(CategoryFactory)

class PostModelFactoryBoyTest(TestCase):
    def test_post_creation(self):
        post = PostFactory()
        self.assertTrue(isinstance(post,Post))
        self.assertEqual(str(post.category),'testcategory')

