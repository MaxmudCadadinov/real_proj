
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import Loginform, regist_form, photo
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from myapp.models import User, Photo
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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
                user = User.objects.filter(name=username, password=password).first()
                pk = user.id
                return redirect('profile', user=pk)

            else:
                return redirect('/regis')

           
    else:
        form = Loginform()

    return render(request, 'myapp/entrance.html', {'form': form})

###
@csrf_protect
def profile(request, user):
    
    user = User.objects.filter(id = user).first()
    name = user.name
    user_id = user.id
    box = {'user': user_id, 'user_name': name}
    
    return render(request, 'myapp/profile.html', box)

@csrf_protect
def photos(request, user):
    if request.method == 'POST':
        form = photo(request.POST, request.FILES)  # Используйте request.FILES
        if form.is_valid():
            photoname = form.cleaned_data['photo']
            user_instance = User.objects.get(id=user)
            savephoto = Photo(image=photoname, user=user_instance)
            savephoto.save()
            messages.success(request, 'Фотография успешно загружена!')
            return redirect('photos', user=user)
        else:
            messages.error(request, 'Ошибка при загрузке фотографии')
    else:
        form = photo()
        all_photos = Photo.objects.filter(user_id=user)
    return render(request, 'myapp/photos.html', {'form': form, 'all_photos': all_photos})
###                                                                                         



###



@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = regist_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User(user_name = username, password = password)
            user.save()

    else:
        form = regist_form()

    return render(request, 'myapp/regis.html', {'form': form})



    



                                                                                            
