from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from blog.views import about_me, posts_list, contact, PostsList


class AboutMePageTest(TestCase):
    def test_about_me_url_resolves_to_about_me_view(self):
        found = resolve('/aboutme/')
        self.assertEqual(found.func, about_me)

    def test_about_me_returns_correct_html(self):
        request = HttpRequest()
        response = about_me(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>About me</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


class BlogPageTest(TestCase):
    def test_blog_url_resolves_to_posts_list_view(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, posts_list)

        #  def test_blog_returns_correct_html(self):
        #  request = HttpRequest()
        #  response = posts_list(request)
        #  self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        #  self.assertIn(b'<title>Blog</title>', response.content)
        #  self.assertTrue(response.content.endswith(b'</html>'))


class ContactPageTest(TestCase):
    def test_contact_page_url_resolves_to_contact_view(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, contact)

    def test_contact_returns_correct_html(self):
        request = HttpRequest()
        response = contact(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>Contact me</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


class AllPhotosPageTest(TestCase):
    def test_all_photos_url(self):
        found = resolve('/photos/')
        self.assertEqual(found.func, 'photologue.urls')
