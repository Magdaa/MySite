from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Post, Tag
import datetime
import psycopg2


def index(request):
    num_posts = Post.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_posts': num_posts},
    )


def view_post(request):
    posts = Post.objects.all().order_by('-posted')
    return render_to_response('homepage.html',
                              {'posts': posts})
    #  context_instance=RequestContext(request))


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
