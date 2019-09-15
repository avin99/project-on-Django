from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from .models import *
from .models import dish
# User=get_user_model()

class SignUpForm(forms.ModelForm):
    first_name=forms.CharField(max_length=30,required=False,help_text='Optional. ')
    last_name=forms.CharField(max_length=30,required=False,help_text='Optional.')
    email=forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.')
    is_owner=forms.BooleanField()
    
    # def save(self, commit=True):
    #     owner = self.cleaned_data.get('owner', None)
       
    #     return super(SignUpForm, self).save(commit=commit)
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password','is_owner') 

class dishform(forms.ModelForm):
    class Meta:
        model = dish
        fields=('restaurant_address','name_of_dish','price','image',)

            
            
            
            
        