from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone

from .models import *
from .forms import *

def article(request):
    articles =  Article.objects.all()
    context = {
        "articles" : articles,
        "title" : "My Article",
    }
    return render(request, 'articles/index.html', context)

def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {"article": article}
    return render(request, 'articles/details.html',  context)

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article')
    else:
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form':form})

def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('article')
    else:
        form = ArticleForm(instance=article)
        return render(request, 'articles/edit.html', {'form':form})

def delete_article(request, article_id):
    Article.objects.filter(id=article_id).delete()
    return redirect('article')

def like_article(request, article_id):
    if article_id:
        article = Article.objects.get(id=article_id)
        count = article.likes
        count += 1
        article.likes = count
        article.save()
    return redirect(request.META['HTTP_REFERER'])
    
def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()
            return redirect('article_id', article_id=a.id)
    else:
        form = CommentForm()
        args = {}
        args['form'] = form
        args['article'] = a
        return render(request, 'articles/add_comment.html', args)

def search_article(request):
    if request.method == "POST":
        search_text = request.POST['search_text']    
    else:
        search_text = ''

    articles = Article.objects.filter(title__icontains=search_text)

    context = {"articles" : articles}

    return render(request, 'articles/index.html', context)


def search_article2(request):
    if request.method == "POST":
        search_text = request.POST['search_text']    
    else:
        search_text = ''

    articles = Article.objects.filter(title__icontains=search_text)

    context = {"articles" : articles}

    return render(request, 'articles/index.html', context)