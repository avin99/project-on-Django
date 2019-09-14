from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.models import AbstractUser
from.forms import SignUpForm
admin.site.register(User)
