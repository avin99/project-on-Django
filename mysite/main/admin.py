from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,dishes,UserProfile
from django.contrib.auth.models import AbstractUser
from .forms import SignUpForm1,dishform,SignUpForm2
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(dishes)

#fields = ['image_tag']
#readonly_fields = ['image_tag']