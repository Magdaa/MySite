from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from .forms import CommentForm

from blog.models import Post, Tag, Category
from blog.forms import ContactForm
import datetime


def index(request):
    num_posts = Post.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_posts': num_posts},
    )


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def about_me(request):
    return render(request, 'about_me.html')


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
    return render(request, 'contact_form.html', {'form': form})


class PostsList(ListView):
    model = Post
    template_name = 'blog.html'
    paginate_by = 5
    queryset = Post.objects.all().order_by('-posted')


class PostsDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CategoryList(ListView):
    model = Category
    template_name = 'categories.html'


class CategoryPosts(ListView):
    model = PostsList
    template_name = 'posts_from_category.html'
    queryset = Post.objects.filter(category__name=Post.category)


post_detail = PostsDetailView.as_view()
posts_list = PostsList.as_view()
category_list = CategoryList.as_view()
post_by_category = CategoryPosts.as_view()


def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


def get_post_by_category(request, name):
    posts = Post.objects.all().order_by('-pub_date')
    category = Category.objects.all()
    category_posts = []
    for post in posts:
        if post.category.filter(name=name):
            category_posts.append(post)
    pages = Paginator(category_posts, 5)
    category = Post.objects.filter(name=name)[0]
    return render_to_response('posts_from_category.html', {'category': category})




