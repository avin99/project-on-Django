from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import SignUpForm
from .forms import dishform
from .models import dish
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
        
        use = request.POST.get("username")
        ema= request.POST.get("email")
        pas= request.POST.get("password")
        is_own = request.POST.getlist("is_owner")
        o_ref=Userdetails(username=use,email=ema,password=pas,is_owner=is_own)
        o_ref.save()
    return render(request,'main/signup.html')

def dish_detail_view(request):
    if request.method == "POST":
        form = dishform(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request,'main/dishlist.html')
    else:
        form = dishform()
        
    context={
            'form' : form,
            
    }
    return render(request,'main/dishdetail.html',context)


def dish_list_view(request):
    obj = dish.objects.all()
    return render(request,'main/dishlist.html',{'obj':obj})


   

    
