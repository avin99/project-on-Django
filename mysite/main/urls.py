from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import dish_detail_view

app_name='main'
urlpatterns=[
    path("",views.homepage,name="homepage"),
    path('register_as_customer',views.register_as_customer,name="register_as_customer"),
    path('register_as_owner',views.register_as_owner,name="register_as_owner"),
    path('login/',views.login_request,name="login.url"),
    path('dishlist/',views.dish_list_view,name="dishlist"),
    path('dishdetail/',views.dish_detail_view,name='dishdetail'),
    path('logout/',views.logout_request,name="logout"),
   
    path('customer_profile/',views.customer,name="customer"),
    path('restaurant_profile/',views.restaurant,name="restaurant"),
    #path("<single_slug>",views.single_slug,name="single_slug")
]