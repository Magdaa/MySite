"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from blog.views import *

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  #url(r'^blog/categories/', category_list, name='categories'),
                  url(r'^blog/categories/travels', post_by_category, name='posts_from_category'),
                  url(r'^blog/(?P<slug>[\w\-]+)/$', post_detail, name='post-detail'),
                  url(r'^blog/(?P<slug>[\w\-]+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
                  url(r'^blog', posts_list, name='blog'),
                  url(r'^index/$', index, name='index'),
                  url(r'^search/$', search),
                  url(r'^contact/$', contact, name='contact'),
                  url(r'^aboutme/', about_me, name='aboutme'),
                  #url(r'^photos/', include('photologue.urls', namespace='photologue')),
                  url(r'photos/', include('photologue.urls', namespace="photologue"), name='gallery_list')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)