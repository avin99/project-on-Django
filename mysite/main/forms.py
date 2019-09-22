from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from .models import *

User=get_user_model()

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
    image =forms.ImageField()
    location=forms.CharField(max_length=100)
    # def save(self, commit=True):
    #     owner = self.cleaned_data.get('owner', None)
       
    #     return super(SignUpForm, self).save(commit=commit)
    
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2','is_owner','image','location') 

class dishform(forms.ModelForm):

    class Meta:
        model = dishes
        fields=('address','description','dish_name','price','image')

class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields =(
                'email',
                'first_name',
                'last_name',
                'image',
                )


            
            
        