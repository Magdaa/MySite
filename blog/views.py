from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from blog.models import Post, Tag, Category
from blog.forms import ContactForm
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
    return render_to_response('blog.html',
                              {'posts': posts})


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def view_category(request):
    categories = Category.objects.all()
    return render_to_response('homepage.html',
                              {'categories': categories})


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            posts = Post.objects.filter(body__icontains=q)
            return render(request, 'search_results.html',
                          {'posts': posts, 'query': q})

    return render(request, 'search_form.html', {'error': error})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['magda.ant@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form':
                                                     form})


class PostsList(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'blog'


posts_list = PostsList.as_view()


class PostsDetailView(DetailView):
    model = Post


post_detail = PostsDetailView.as_view()
