from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts, "title":"Latest Posts"}
    return render(request, 'posts/index.html',  context)

def details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post}
    return render(request, 'posts/details.html',  context)