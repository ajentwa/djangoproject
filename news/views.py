from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q

from .models import *
from .forms import *

def news_view(request):
    url_parameter = request.GET.get("q")

    if url_parameter:
        lookups = Q(title__icontains=url_parameter) | Q(description__icontains=url_parameter) | Q(author__icontains=url_parameter) 
        news = News.objects.filter(lookups)
    else:
        news = News.objects.order_by('-pub_date')

    context = {"news": news }

    if request.is_ajax():
        html = render_to_string(
            template_name="news/mynews.html", 
            context={"news": news}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "news/index.html", context)
    
def register(request):

    context = {"form": RegistrationForm}

    return render(request, 'accounts/register.html', context)


# def addUser(request):
#     if  request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('index')

#     else:
#         form = RegistrationForm()
#         return render(request, 'accounts/register.html', {"form":form})


def addUser(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            register = Registration(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
            )
            register.save()
            messages.add_message(request, messages.SUCCESS, "You are registered now you can login in")

        return redirect('login')


def addNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "News has been added successfully")
            return redirect('news_view')
    else:
        form = NewsForm()
        return render(request, 'news/add_news.html', {"form":form})
