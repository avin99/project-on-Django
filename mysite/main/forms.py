from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from .models import *

# User=get_user_model()

class SignUpForm1(UserCreationForm):
    first_name=forms.CharField(max_length=30,required=False,help_text='Optional. ')
    last_name=forms.CharField(max_length=30,required=False,help_text='Optional.')
    email=forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.')
    is_customer=forms.BooleanField()

    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2','is_customer') 

class SignUpForm2(UserCreationForm):
    first_name=forms.CharField(max_length=30,required=False,help_text='Optional. ')
    last_name=forms.CharField(max_length=30,required=False,help_text='Optional.')
    email=forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.')
    is_owner=forms.BooleanField()
    # def save(self, commit=True):
    #     owner = self.cleaned_data.get('owner', None)
       
    #     return super(SignUpForm, self).save(commit=commit)
    
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2','is_owner') 

class dishform(forms.ModelForm):

    class Meta:
        model = dishes
        fields=('dish_name','price','image')

class Restform(forms.ModelForm):
    
    class Meta:
        model = Restaurant
        fields=('street','telephone','description')
#class UserUpdateForm(forms.ModelForm):
    #email=forms.EmailField()
    #class Meta:
      #  model = User
       # fields =['username,email']

#class ProfileUpdateForm(forms.ModelForm):
   # class Meta:
     #   model = Profile
      #  field = ['image']

            
            
        