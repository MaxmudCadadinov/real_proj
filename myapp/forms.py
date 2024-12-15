from django import forms
#from django.contrib.auth.models import User
from django.db import models


class Loginform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class regist_form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField()
    
class photo (forms.Form):
    photo = forms.ImageField(label='Выберите изображение')
    
