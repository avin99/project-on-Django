from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

User=get_user_model()

class SignUpForm(forms.ModelForm):
    first_name=forms.CharField(max_length=30,required=False,help_text='Optional. ')
    last_name=forms.CharField(max_length=30,required=False,help_text='Optional.')
    email=forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.')
    customer=forms.BooleanField()
    owner=forms.BooleanField()
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password','customer','owner') 