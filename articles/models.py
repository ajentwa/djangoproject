from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to="photos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
