
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import Loginform, regist_form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from myapp.models import User




###
@csrf_protect
def  entrance(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(name=username, password=password).exists()
            if user:
                pass
            else:
                return redirect('/regis')

           
    else:
        form = Loginform()

    return render(request, 'myapp/entrance.html', {'form': form})

###      
@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = regist_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            telefon = form.cleaned_data['tel']        
            
            user = User(user_name = username, password = password, email = email, tel = telefon)
            user.save()

    else:
        form = regist_form()

    return render(request, 'myapp/regis.html', {'form': form})

###
def profile(request):   
    return render




