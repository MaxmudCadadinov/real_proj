from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=100)

class regis(models.Model):
    user_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    tel = models.CharField(max_length=70)


