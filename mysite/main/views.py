from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm1,dishform,SignUpForm2
from .forms import dishesform
from .models import dishes,Restaurant_name
from django.views.generic import TemplateView
from django.forms import modelformset_factory
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.

def customer(request):
    obj = Restaurant_name.objects.all()
    return render(request,"main/customer_profile.html",{'obj':obj})

def restaurant(request):
    if request.method == "POST":
        form = dishform(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username=request.user
            instance.save()
            return render(request,"main/restaurant_profile.html")
        else:
            return render(request,"main/restaurant_profile.html",{'form' : form})
    form = dishform()
    return render(request,"main/restaurant_profile.html",{'form':form})


def homepage(request):
    return render(request,template_name="main/home.html",context={'Restaurant_name':Restaurant_name.objects.all()})


def register_as_customer(request):
    if request.method == "POST":
        form = SignUpForm1(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'main/login.html')
        else:
            form=SignUpForm1()
        return render(request,'registration/register.html',{'form':form})
    form=SignUpForm1()
    return render(request,'registration/register.html',{'form':form})

def register_as_owner(request):
    if request.method == "POST":
        form = SignUpForm2(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'main/login.html')
        else:
            form=SignUpForm2()
        return render(request,'registration/register.html',{'form':form})
    form=SignUpForm2()
    return render(request,'registration/register.html',{'form':form})

def dish_detail_view(request,):
    if request.method == "POST":
        form = dishesform(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request,'main/dishlist.html')
    else:
        form = dishesform()
        
    context={
            'form' : form
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
    
#def single_slug(request,single_slug):
#restaurant = [c.restaurant_slug for c in Resataurant_name.objects.all()]
   # if single_slug in restaurant:
       # return redirect(request,'main/dishlist.html')

def logout_request(request):
    logout(request)
    return redirect("main:homepage")


def login_request(request):                                                            
    
    if request.method == 'POST':                                             #if user hits the login button
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():                                                  #if the form is valid
            username = form.cleaned_data.get('username')                     #saving the username form the form
            password = form.cleaned_data.get('password')                     #saving the password from the form
            user = authenticate(username=username, password=password)        #authenticating the user i.e. username and passwords match simultaneously with a user's profile in database
            if user is not None:                                             #basically means "if user is true i.e. if user is successfully authenticated"
                login(request, user)                                         #log the user into the session
                #messages.info(request, f"You are now logged in as {username}")    #display a message that user is logged in
                if user.is_owner:
                    return redirect("main:restaurant")

                else: 
                    return redirect("main:customer")                              
            else:                                                            #if it fails to authenticate
                messages.error(request, "Invalid username or password.")     #display an error message

        else:                                                                #if the form is not valid
           messages.error(request, "Invalid username or password.")         #display the error message

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})