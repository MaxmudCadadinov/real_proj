from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=100)

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')