from django.urls import path
from . import views

urlpatterns = [
    path('', views.article, name='article'),
    path('<int:article_id>', views.view_article, name='article_id'),
    path('create_article', views.create_article, name='create_article'),
    path('edit_article/<int:article_id>', views.edit_article, name='edit_article'),
    path('delete_article/<int:article_id>', views.delete_article, name='delete_article'),
    path('likes/<int:article_id>', views.like_article, name='like_article'),
    path('comment/<int:article_id>', views.add_comment, name='add_comment'),
    path('search', views.search_article, name='search_article'),
    path('search2', views.search_article2, name='search_article2'),
]