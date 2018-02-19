

import pytest
from blog.models import Post


def test_string_representation_pytest():
    post = Post(title='Fake title')
    assert str(post) == 'Fake title'
def test_absolute_url():
    post = Post(slug='test-slug')
    returned_slug = post.get_absolute_url()
    assert returned_slug == '/blog/test-slug/'
