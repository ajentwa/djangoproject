from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_view, name='news_view'),
    path('signup', views.register, name='register2'),
    path('addUser', views.addUser, name='addUser'),   
    path('addNews', views.addNews, name='addNews'),   
]







