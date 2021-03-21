from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils.safestring import mark_safe

# Create your models here.
from category.models import Category


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=13)
    slug = models.SlugField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)

    # image = models.FileField(upload_to='images', blank=True)
    def admin_photo(self):
        return mark_safe('<img src="{}" width="150" />'.format(self.image.url))
    admin_photo.short_description = "Image"
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title + ' by ' + self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
