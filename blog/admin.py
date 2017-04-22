from django.contrib import admin
from blog.models import Post, Tag, Category
from django import forms


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted', 'category')
    prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
