from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm1,dishform,SignUpForm2
from .models import dishes,User
from django.views.generic import TemplateView,CreateView
from django.forms import modelformset_factory
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.views.generic import DetailView
from .forms import dishform
from django.http import HttpResponse
# Create your views here.


def customer(request):
    obj = User.objects.filter(id__gte=0)
    return render(request,"main/customer_profile.html",{'obj':obj})
  

#class RestaurantCreate(CreateView):
   # model = Restaurant
    #template_name = 'main/restaurant_profile.html'
    #form_class = Restform
#def form_valid(self, form):
    #form.instance.user = self.request.user
    #return super(RestaurantCreate, self).form_valid(form)

def restaurant(request):
    if request.method == "POST":
        form = dishform(request.POST or None,request.FILES or None)
        if form.is_valid():
            dish_profile = form.save(commit=False)
            dish_profile.username= request.user
            dish_profile.save()
            return redirect("main:homepage")
        else:
            return render(request,'main/add_restaurant.html',{'form':form})
    form = dishform()
    return render(request,'main/add_restaurant.html',{'form':form})

#def Profile(request):
  #  return render(request,template_name="main/profile.html",{'Restaurant_name':Restaurant_name.objects.all()})

def homepage(request):
    
    return render(request,template_name="main/home.html",context={'dishes':dishes.objects.all()})


def register_as_customer(request):
    if request.method == "POST":
        form = SignUpForm1(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'main/login.html')
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
            return render(request,'main/login.html')
        else:
            form=SignUpForm2()
        return render(request,'main/signup.html',{'form':form})
    form=SignUpForm2()
    return render(request,'main/signup.html',{'form':form})

def dish_list_view(request):
    obj = dishes.objects.all()
    return render(request,'main/dishlist.html',{'obj':obj})

def rest_detail_view(request,):
    if request.method == "POST":
        form = dishform(request.POST or None,request.FILES or None)
        if form.is_valid():
            custom = form.save(commit=False)
            custom.username = request.user
            custom.save()
            return render(request,'main/home.html')
    else:
        form = dishform()
        
    context={
            'form' : form,
    }
    return render(request,'main/dishd.html',context)
    
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

def profile(request):
    if request.method=='POST':
        u_form = SignUpForm2(request.POST,instance=request.user)
        #p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid(): #and p_form.is_valid():
            u_form.save()
            #p_form.save()
    else:
        u_form = SignUpForm2(instance=request.user)
        #p_form = ProfileUpdateForm(request.FILES,instance=request.user.profile)
        context={
            'u_form':u_form,
            #'p_form' : p_form,
        }
    return render(request,'main/profile.html',context)
 
#def Create_view(request):
    #if request.method=='POST':
      #  username=request.POST.GET("username")
       # email = request.POST.get("email")
       # password =request.POST.get("password")
       # is_owner =request.POST.get("is_owner")
       # return render(request,'main/login.html')

def County_Details(request,pk):
    d = dishes.objects.filter(username__pk=pk)
    return render(request, 'main/restdetail.html', {'d': d})

def addrestaurant(request):
    if request.method == "POST":
        form = Restform(request.POST or None,request.FILES or None)
        if form.is_valid():
            own = form.save(commit=False)
            own.restaurant_name= request.user
            own.save()
            return render(request,'main/restaurant_profile.html')
    else:
        form = Restform()
        
    context={
            'form' : form,
    }
    return render(request, 'main/add_restaurant.html',context)