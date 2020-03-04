from django.urls import path

from . import views

urlpatterns = [
    path('', views.contactPage, name="contactPage"),
    path('ajax/contact', views.postContact, name ='contact_submit'),
]