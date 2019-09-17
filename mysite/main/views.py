from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import SignUpForm,dishform
from .forms import dishesform
from .models import dishes,Restaurant_name
from django.views.generic import TemplateView
from django.forms import modelformset_factory
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

def indexView(request):
    
    return render(request,"index.html")

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'login.html')
        else:
            form=SignUpForm()
        return render(request,'main/signup.html',{'form':form})
    form=SignUpForm()
    return render(request,'main/signup.html',{'form':form})


def dish_detail_view(request,):
    if request.method == "POST":
        form = dishesform(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request,'main/dishlist.html')
    else:
        form = dishesform()
        
    context={
            'form' : form,
    }
    return render(request,'main/dishdetail.html',context)


def dish_list_view(request):
    obj = dishes.objects.all()
    return render(request,'main/dishlist.html',{'obj':obj})

def rest_detail_view(request,):
    if request.method == "POST":
        form = dishform(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request,'main/restlist.html')
    else:
        form = dishform()
        
    context={
            'form' : form,
    }
    return render(request,'main/restdetail.html',context)

def rest_list_view(request):
    obj = Restaurant_name.objects.filter(username=request.user)
    return render(request,'main/restlist.html',{'obj':obj})
    
def single_slug(request,single_slug):
    restaurant = [c.restaurant_slug for c in Resataurant_name.objects.all()]
    if single_slug in restaurant:
        return redirect(request,'main/dishlist.html')



