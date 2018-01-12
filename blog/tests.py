from django.test import LiveServerTestCase, Client
from django.test import TestCase
from django.utils import timezone
from blog.models import Post, Category


class PostTest(TestCase):
    def test_create_post(self):
        post = Post()
        category=Category()
        post.title = 'My first post'
        post.body = 'That is my first real post'
        Category.name = 'life'
        post.posted = timezone.now()
        post.save()

        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.body, 'That is my first real post')
        self.assertEquals(only_post.posted.day, post.posted.day)
        self.assertEquals(only_post.posted.month, post.posted.month)
        self.assertEquals(only_post.posted.year, post.posted.year)
        self.assertEquals(only_post.posted.hour, post.posted.hour)
        self.assertEquals(only_post.posted.minute, post.posted.minute)
        self.assertEquals(only_post.posted.second, post.posted.second)


class AdminTest(LiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(('Log in').encode('utf-8') in response.content)
        self.client.login(username='testuser', password='Testing123')
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)
        # self.assertTrue(('Log out').encode('utf-8') in response.content)

    def test_logout(self):
        self.client.login(username='testuser', password='Testing123')
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)
        # self.assertTrue(('Log out').encode('utf-8') in response.content)
        self.client.logout()
        response = self.client.get('/admin/', follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(('Log in').encode('utf-8') in response.content)

    def test_create_post(self):
        self.client.login(username='testuser', password="Testing123")
        response = self.client.get('/admin/blog/post/add/', follow=True)
        self.assertEquals(response.status_code, 200)
        data = {'title': 'My first post',
                'body': 'This is my first post',
                'posted_0': '2013-12-28',
                'posted_1': '22:00:04',
                'tags': '2',
                '_save': 'Save'}
        response = self.client.post('/admin/blog/post/add/', data=data, auth=('testuser', "Testing123"),
                                    content_type='text/html', follow=True, secure='false')
        self.assertEquals(response.status_code, 200)
        # self.assertTrue(('added successfully').encode('utf-8') in response.content)
        all_posts = Post.objects.all()
        # self.assertEquals(len(all_posts), 1)
