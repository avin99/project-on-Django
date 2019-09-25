from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm1,dishform,SignUpForm2,EditProfileForm
from .models import dishes,User,UserProfile
from django.views.generic import TemplateView,CreateView
from django.forms import modelformset_factory
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.views.generic import DetailView
from .forms import dishform
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
# Create your views here.
#customer_profile.html

from django.contrib.auth import get_user_model
User = get_user_model()

class customer(View):
    def get(self,request):
        obj = User.objects.filter(is_owner=True)
        query = request.GET.get("q")
        if query:
            
            obj = User.objects.filter(obj__icontains = query)
        return render(request,'main/restaurantdetail.html',{'obj':obj})



# def customer(request):
    # obj = User.objects.filter(is_owner=True)
    # return render(request,'main/restaurantdetail.html',{'obj':obj})
  

#class RestaurantCreate(CreateView):
   # model = Restaurant
    #template_name = 'main/restaurant_profile.html'
    #form_class = Restform
#def form_valid(self, form):
    #form.instance.user = self.request.user
    #return super(RestaurantCreate, self).form_valid(form)

def owner_profile(request):
    d = dishes.objects.filter(username = request.user)
    return render(request,'main/owner_info.html',{'d':d})


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

class homepage(View):
    def get(self,request):
        b = User.objects.filter(location = 'Delhi')
        c = User.objects.filter(location = 'Bangalore')
        return render(request,template_name="main/index.html",context={'dishes':dishes.objects.all()})


    # def homepage(request):
    #     b = User.objects.filter(location = 'Bangalore')
    #     return render(request,template_name="main/index.html",context={'dishes':dishes.objects.all()})

# class register_as_customer(View):
#     form_class=SignUpForm1
#     initial={'key':'value'}
#     template_name="main/signup1.html"

#     def get(self,request):
#         form=self.form_class(initial=self.initial)
#         return render(request,self.template_name,{'form':form})

#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'main/index.html')
#         else:
#             form=self.form_class(initial=self.initial)
#             return render(request,template_name,{'form':form}) 

# def register_as_customer(request):
#     if request.method == "POST":
#         form = SignUpForm1(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'main/index.html')
#         else:
#             form=SignUpForm1()
#         return render(request,'main/signup1.html',{'form':form})
#     form=SignUpForm1()
#     return render(request,'main/signup1.html',{'form':form})
def register_as_customer(request):
    if request.method == 'POST':
        form = SignUpForm1(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('main/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm1()
    return render(request, 'main/signup1.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        # print(user)
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        print(user.is_active)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid,"uid")
        # x = User.objects.filter(pk=uid)
        # print(x,"hi")
        return HttpResponse('Activation link is invalid!')

class register_as_owner(View):
    form_class=SignUpForm2
    initial={'key':'value'}
    template_name="main/signup.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST or None,request.FILES or None)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            
            return render(request,'main/index.html')
        else:
            form=self.form_class(initial=self.initial)
            return render(request,template_name,{'form':form})

# def register_as_owner(request):
#     if request.method == "POST":
#         form = SignUpForm2(request.POST or None,request.FILES or None)
#         if form.is_valid():
#             form.save()
#             return render(request,'main/index.html')
#         else:
#             form=SignUpForm2()
#         return render(request,'main/signup.html',{'form':form})
#     form=SignUpForm2()
#     return render(request,'main/signup.html',{'form':form})

class dish_list_view(View):

    def get(self,request):

        obj = dishes.objects.all()
        return render(request,'main/dishlist.html',{'obj':obj})

class rest_detail_view(View):
    form_class = dishform
    initial={'key':'value'}
    template_name="main/dishd.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request,'main/index.html')
        else:
            form=self.form_class(initial=self.initial)
            return render(request,template_name,{'form':form})
    # if request.method == "POST":
    #     form = dishform(request.POST or None,request.FILES or None)
    #     if form.is_valid():
    #         custom = form.save(commit=False)
    #         custom.username = request.user
    #         custom.save()
    #         return render(request,'main/home.html')
    # else:
    #     form = dishform()
        
    # context={
    #         'form' : form,
    # }
    # return render(request,'main/dishd.html',context)
    
class logout_request(View):
    def get(self,request):

        logout(request)
        return redirect("main:homepage")


class login_request(View):
    form_class = AuthenticationForm
    initial={'key':'value'}
    template_name="main/login.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')                     #saving the username form the form
            password = form.cleaned_data.get('password')                     #saving the password from the form
            user = authenticate(username=username, password=password)        #authenticating the user i.e. username and passwords match simultaneously with a user's profile in database
            if user is not None:                                             #basically means "if user is true i.e. if user is successfully authenticated"
                login(request, user)                                         #log the user into the session
                messages.info(request, f"You are now logged in as {username}")    #display a message that user is logged in
                if user.is_owner:
                    return redirect("main:owner_profile")
                else: 
                    return redirect("main:customer")                              
            else:                                                            #if it fails to authenticate
                 messages.error(request, "Invalid username or password.")     #display an error message
                 form=self.form_class(initial=self.initial)
                 return render(request,self.template_name,{'form':form})
        else:                                                                #if the form is not valid
            form=self.form_class(initial=self.initial)
            return render(request,self.template_name,{'form':form})

# def login_request(request):                                                            
#     if request.method == 'POST':                                             #if user hits the login button
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#                                                               #if the form is valid
#             username = form.cleaned_data.get('username')                     #saving the username form the form
#             password = form.cleaned_data.get('password')                     #saving the password from the form
#             user = authenticate(username=username, password=password)        #authenticating the user i.e. username and passwords match simultaneously with a user's profile in database
#             if user is not None:                                             #basically means "if user is true i.e. if user is successfully authenticated"
#                 login(request, user)                                         #log the user into the session
#                 messages.info(request, f"You are now logged in as {username}")    #display a message that user is logged in
#                 if user.is_owner:
#                      return redirect("main:restaurant")
#                 else: 
#                      return redirect("main:customer")                              
#             else:                                                            
#                  messages.error(request, "Invalid username or password.")     

#         else:                                                               
#             messages.error(request, "Invalid username or password.")        

#     form = AuthenticationForm()
#     return render(request = request,
#                     template_name = "main/login.html",
#                     context={"form":form})

def edit_profile(request):
    if request.method=='POST':
        u_form = EditProfileForm(request.POST,request.FILES,instance=request.user)
        #p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid(): #and p_form.is_valid():
            u_form.save()
    else:
        u_form = EditProfileForm(instance=request.user)
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
    return render(request, 'main/dish_info.html', {'d': d})



# def addrestaurant(request):
#     if request.method == "POST":
#         form = Restform(request.POST or None,request.FILES or None)
#         if form.is_valid():
#             own = form.save(commit=False)
#             own.restaurant_name= request.user
#             own.save()
#             return render(request,'main/restaurant_profile.html')
#     else:
#         form = Restform()
        
#     context={
#             'form' : form,
#     }
#     return render(request, 'main/add_restaurant.html',context)

class Best_Delhi(View):
    def get(self,request):

        d = User.objects.filter(location='Delhi')
        return render(request,'main/Best_delhi.html',{'d':d})

class Best_bangalore(View):
    def get(self,request):

        d=User.objects.filter(location='Bangalore')
        return render(request,'main/Best_bangalore.html',{'d':d})
    
class Best_Mumbai(View):
    def get(self,request):

        d=User.objects.filter(location='Mumbai')
        return render(request,'main/Best_mumbai.html',{'d':d})

class Best_Pune(View):
    def get(self,request):

        d=User.objects.filter(location='Pune')
        return render(request,'main/Best_Pune.html',{'d':d})

def delete_rest(request,pk):
    if request.method=='POST':
        rest = rest.objects.get(pk=pk)
        rest.delete()
        return render(request,'main/owner_info.html',{'rest':rest})
