from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from accounts.forms import SignUpForm
from.models import post
# Create your views here.

def indexView(request):
    
    dests = post.objects.all()
    return render(request,"index.html",{'dests':dests})

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
            

    else:
        form=SignUpForm()
    return render(request,'signup.html',{'form':form})