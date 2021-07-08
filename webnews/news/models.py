from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)


class News(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    detail = models.TextField(default='')
    image = models.ImageField(upload_to='images')
    date_added = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField(default='')
    date_added = models.DateTimeField(auto_now_add=True)
