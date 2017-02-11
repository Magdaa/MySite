from django.contrib import admin
from blog.models import Blog, Category, Tag
from django import forms

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
