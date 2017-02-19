from django.contrib import admin
from blog.models import Post, Tag
from django import forms

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']


admin.site.register(Post)
admin.site.register(Tag)
