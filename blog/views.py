from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Post, Tag
import datetime
import psycopg2



def index(request):
    return render_to_response('index.html', {
        'posts': Post.objects.all()[:5]
    })


def view_post(request):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post)
    })



def homepage(request):
    return render(request, 'homepage.html')


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
