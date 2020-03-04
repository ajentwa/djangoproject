from django import forms
from .models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter Username'
                              }))
    password = forms.CharField(max_length=200,
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter Password'
                              }))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter Email'
                              }))
    phone = forms.CharField(max_length=100,
                            widget=forms.NumberInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter Phone'
                              }))


class NewsForm(forms.ModelForm):
      class Meta:
            model = News
            fields = "__all__"
            # fields = ['author','title','description','pub_date']
            widgets = {
                  'author':forms.TextInput(attrs={
                           'class':'form-control',
                           'placeholder':'Author'
                              }
                          ),
                  'title':forms.TextInput(attrs={
                           'class':'form-control',
                           'placeholder':'Title'
                              }
                          ),
                  'description':forms.Textarea(attrs={
                           'class':'form-control',
                           'placeholder':'Comment here'
                              }
                          ),
                  'pub_date':forms.DateInput(attrs={
                           'class':'form-control',
                           'placeholder':'Date in YYYY-MM-DD'
                              }
                          ),
            }
      










# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Registration
#         fields = "__all__"


