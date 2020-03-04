from django import forms

from .models import *

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = ('title','body','pub_date','thumbnail')
        exclude = ('likes',)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name','body')


        
