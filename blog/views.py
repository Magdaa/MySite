from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Blog, Category, Tag
import datetime



def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })


def homepage(request):
    return render(request, 'homepage.html')


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
