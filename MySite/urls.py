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
                  url(r'^homepage/$', current_datetime, name='home'),
                  url(r'^time/', current_datetime),
                  url(r'^blog/category/$', view_category, name='category'),
                  url(r'^blog/(?P<slug>[\w\-]+)/$', post_detail,name='post-detail'),
                  url(r'^blog', posts_list, name='blog'),
                  url(r'^index/$', index, name='index'),
                  url(r'^search/$', search),
                  url(r'^contact/$', contact, name='contact'),
                  url(r'^aboutme/', about_me, name='aboutme'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)