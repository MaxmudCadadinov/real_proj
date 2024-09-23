from django.urls import path
from . import views
urlpatterns = [
 path('', views.entrance, name='index'),
 path('regis/', views.registration, name='regis'),
 
]