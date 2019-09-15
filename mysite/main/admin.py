from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,dish,Userdetails
from django.contrib.auth.models import AbstractUser
from .forms import SignUpForm,dishform
admin.site.register(Userdetails)
class dishAdmin(admin.ModelAdmin):
    form = dishform

admin.site.register(dish, dishAdmin)
#fields = ['image_tag']
#readonly_fields = ['image_tag']