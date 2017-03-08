from django.db import models


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
    # slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField()
    tags = models.ManyToManyField(Tag, verbose_name='tags')
    category = models.ForeignKey(Category, default=1, verbose_name='categories')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['posted']
