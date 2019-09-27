from django.db import models
from django.contrib.auth.models import AbstractUser
from time import time
from django.dispatch import receiver
from django.db.models.signals import post_save

def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s" % str((time()).replace('.','_'),filename)

class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics',default="")
    location = models.CharField(max_length=100,default="")

class dishes(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=100)
    description = models.TextField(default="",)
    dish_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
   
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.IntegerField()
    image = models.ImageField(upload_to='pics')

def __str__(self):

    return self.user

def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    phone = models.CharField(max_length=111, default="")      


class OrderStatus(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."    













