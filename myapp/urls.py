from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path('', views.entrance, name='index'),
path('regis/', views.registration, name='regis'),
path('profile/<int:user>/', views.profile, name='profile'), 
path('photos/<int:user>/', views.photos, name='photos'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)