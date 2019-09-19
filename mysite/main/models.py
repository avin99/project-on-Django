from django.db import models
from django.contrib.auth.models import AbstractUser
from time import time

def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s" % str((time()).replace('.','_'),filename)

class User(AbstractUser):
    is_owner=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)

class Restaurant(models.Model):
    restaurant_name = models.OneToOneField(User,on_delete=models.CASCADE)
    street = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    description = models.TextField(default="")

    

class dishes(models.Model):
    username = models.ForeignKey(Restaurant,on_delete=models.CASCADE,max_length=200)
    dish_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')

   
