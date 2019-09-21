from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView

app_name='main'
urlpatterns=[
    path("",views.homepage,name="homepage"),
    path('register_as_customer',views.register_as_customer,name="register_as_customer"),
    path('register_as_owner',views.register_as_owner,name="register_as_owner"),
    path('login/',views.login_request,name="login.url"),
    path('dishlist/',views.dish_list_view,name="dishlist"),
    path('logout/',views.logout_request,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('customer/',views.customer,name="customer"),
    path('add_restaurant/',views.addrestaurant,name="add_restaurant"),
    path('post_a_dish/',views.rest_detail_view,name="rest_detail_view"),
    path('restaurant_profile/',views.restaurant,name="restaurant"),
    url(r'^customer_profile/(?P<pk>\d)/$',views.County_Details, name='County_Details'),
]