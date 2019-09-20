from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,dishes
from django.contrib.auth.models import AbstractUser
from .forms import SignUpForm1,dishform,SignUpForm2
admin.site.register(User)


class dishAdmin(admin.ModelAdmin):
    form = dishform
admin.site.register(dishes,dishAdmin)

#fields = ['image_tag']
#readonly_fields = ['image_tag']