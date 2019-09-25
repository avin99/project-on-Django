from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth.views import LoginView,LogoutView
from main.views import customer,register_as_customer,register_as_owner,dish_list_view,rest_detail_view,logout_request,Best_bangalore,Best_Delhi,Best_Mumbai,login_request,Best_Pune,restaurant

app_name='main'
urlpatterns=[
    path("",views.homepage.as_view(),name="homepage"),
    url(r'^register_as_customer/$',views.register_as_customer,name="register_as_customer"),
    path('register_as_owner',register_as_owner.as_view(),name="register_as_owner"),
    path('login/',login_request.as_view(),name="login.url"),
    path('dishlist/',dish_list_view.as_view(),name="dishlist"),
    path('logout/',logout_request.as_view,name="logout"),
    path('profile/',views.edit_profile,name="profile"),
    path('customer/',customer.as_view(),name="customer"),
    path('post_a_dish/',rest_detail_view.as_view(),name="rest_detail_view"),
    path('restaurant_profile/',views.restaurant,name="restaurant"),
    path('Best_bangalore/',Best_bangalore.as_view(),name="Best_bangalore"),
    path('Best_Delhi/',Best_Delhi.as_view(),name="Best_Delhi"),
    path('Best_Mumbai/',Best_Mumbai.as_view(),name="Best_Mumbai"),
    path('Best_Pune/',Best_Pune.as_view(),name="Best_Pune"),
    path('add_restaurant/',views.restaurant,name="add_restaurant"),
    path('owner_profile/<int:pk>/',views.delete_rest, name='delete_rest'),
    url(r'^customer/(?P<pk>\d)/$',views.County_Details, name='County_Details'),
    path('owner_profile/',views.owner_profile, name='owner_profile'),
    path("checkout/", views.checkout, name="Checkout"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]