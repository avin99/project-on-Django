from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from main.views import customer,register_as_customer,register_as_owner,dish_list_view

app_name='main'
urlpatterns=[
    path("",views.homepage.as_view(),name="homepage"),
    path('register_as_customer',register_as_customer.as_view(),name="register_as_customer"),
    path('register_as_owner',register_as_owner.as_view(),name="register_as_owner"),
    path('login/',views.login_request,name="login.url"),
    path('dishlist/',dish_list_view.as_view(),name="dishlist"),
    path('logout/',views.logout_request,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('customer/',customer.as_view(),name="customer"),
    path('add_restaurant/',views.addrestaurant,name="add_restaurant"),
    path('post_a_dish/',views.rest_detail_view,name="rest_detail_view"),
    path('restaurant_profile/',views.restaurant,name="restaurant"),
     path('Best_Delhi/',views.Best_Delhi,name="Best_Delhi"),
    url(r'^customer/(?P<pk>\d)/$',views.County_Details, name='County_Details'),
]