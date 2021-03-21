from django.contrib import admin

from .models import Post, BlogComment
from category.models import Category


class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'admin_photo','category', 'author', 'timeStamp',]


# Register your models here.
admin.site.register(Post,AdminPost)
admin.site.register(Category)
admin.site.register(BlogComment)
