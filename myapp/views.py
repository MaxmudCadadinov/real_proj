
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import Loginform, regist_form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect





@csrf_protect
def  entrance(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f'получилиии {username}  {password}')
            user = authenticate(request, username=username, password=password)
            if user is  None:
                return redirect('regis')

           
    else:
        form = Loginform()

    return render(request, 'myapp/entrance.html', {'form': form})

       



def registration(request):
    if request.method == 'POST':
        form = regist_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            user = authenticate(request, username=username, password=password, email=email, tel=tel)
            if user is  None:
                print('yesssssssssssssssssssss')

    else:
        form = regist_form()


    
    return render (request,  'myapp/regis.html', {'form': form})




