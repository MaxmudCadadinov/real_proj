from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'myapp/py.html')


def about(request):
    return HttpResponse("About us")
