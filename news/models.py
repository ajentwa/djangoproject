from django.db import models
from django.utils import timezone

class News(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


class SportNews(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.author

class Registration(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.username
    