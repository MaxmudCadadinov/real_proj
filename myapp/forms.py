from django import forms
from django.contrib.auth.models import User



class Loginform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class regist_form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField()
    email = forms.EmailField()
    tel = forms.CharField(max_length=30)


