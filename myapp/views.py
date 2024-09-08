from django.shortcuts import render



# Create your views here.
from django.http import HttpResponse


def index(request):
    # context = {
    #     'image_url1': 'photo_2024-08-26_23-33-31.jpg',
    #     'image_url2': 'photo_2024-08-26_23-33-27.jpg',
    #     'image_url3': 'photo_2024-08-26_23-35-00.jpg'

    #     }
    return render(request, 'myapp/py.html')







def about(request):
    return HttpResponse("About us")

