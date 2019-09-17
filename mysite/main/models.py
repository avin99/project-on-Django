from django.db import models
from django.contrib.auth.models import AbstractUser
from time import time

def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s" % str((time()).replace('.','_'),filename)
class User(AbstractUser):
    is_owner=models.BooleanField(default=False)

class Restaurant_name(models.Model):
    username = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    restaurant_address=models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics',blank=True)
    dish_name=models.CharField(max_length=200)
    price = models.IntegerField()
class dishes(models.Model):
    slug = models.CharField(max_length=50)
    

