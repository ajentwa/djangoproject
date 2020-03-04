from django.urls import path
from . import views 

urlpatterns = [
    path('', views.userPanel, name="userPanel"),
    path('ajax/get_user_info', views.getUserInfo, name = 'get_user_info'),
]