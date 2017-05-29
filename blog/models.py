from django.utils import timezone

from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Tag Type')

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    class Admin:
        list_display = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Category Type')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    class Admin:
        list_display = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')
    body = models.TextField()
    posted = models.DateTimeField()
    # tags=TaggableManager()
    tags = models.ManyToManyField(Tag, verbose_name='tags')
    category = models.ForeignKey(Category, default=1, verbose_name='categories')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['posted']

    def get_absolute_url(self):
        return reverse('post-detail',
                       kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
