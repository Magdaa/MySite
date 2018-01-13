from django.contrib import admin
from blog.models import Post, Tag, Category, Comment
from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery
from django import forms


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted', 'category')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
