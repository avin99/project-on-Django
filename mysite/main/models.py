from django.db import models
from django.contrib.auth.models import AbstractUser
from time import time

def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s" % str((time()).replace('.','_'),filename)
class User(AbstractUser):
    is_owner=models.BooleanField(default=False)
class Userdetails(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=254,help_text='Required. Inform a valid email address.')
    password=models.CharField(max_length=100)
    is_owner=models.BooleanField(default=False)

class dish(models.Model):
    restaurant_address=models.CharField(max_length=100)
    name_of_dish=models.CharField(max_length=50)
    price=models.IntegerField()
    image = models.ImageField(upload_to='pics', blank=True)
    # image=models.FileField(blank=True,upload_to='pics')
    