from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth.views import LoginView,LogoutView
from main.views import customer,register_as_customer,register_as_owner,dish_list_view,rest_detail_view,logout_request,Best_bangalore,Best_Delhi,Best_Mumbai,login_request,Best_Pune,restaurant,edit_dish,owner_edit

app_name='main'
urlpatterns=[
    path("",views.homepage.as_view(),name="homepage"),
    url(r'^register_as_customer/$',register_as_customer.as_view(),name="register_as_customer"),
    path('register_as_owner',register_as_owner.as_view(),name="register_as_owner"),
    path('login/',login_request.as_view(),name="login.url"),
    path('dishlist/',dish_list_view.as_view(),name="dishlist"),
    path('logout/',logout_request.as_view,name="logout"),
    path('profile/',views.edit_profile,name="profile"),
    # path('customer/',customer.as_view(),name="customer"),
    path('post_a_dish/',rest_detail_view.as_view(),name="rest_detail_view"),
    path('restaurant_profile/',views.restaurant,name="restaurant"),
    path('Best_bangalore/',Best_bangalore.as_view(),name="Best_bangalore"),
    path('Best_Delhi/',Best_Delhi.as_view(),name="Best_Delhi"),
    path('Best_Mumbai/',Best_Mumbai.as_view(),name="Best_Mumbai"),
    path('Best_Pune/',Best_Pune.as_view(),name="Best_Pune"),
    path('add_restaurant/',views.restaurant,name="add_restaurant"),
    path('owner_edit/',owner_edit.as_view(),name="owner_edit"),
    path('delete_rest/<int:pk>/',views.delete_rest, name='delete_rest'),
    path('owner_profile/',views.owner_profile, name='owner_profile'),
    url(r'^customer/(?P<pk>\d)/$',views.County_Details, name='County_Details'),
    path('customer/',customer.as_view(),name="customer"),
    #url(r'^customer/(?P<pk>\d)/$',views.County_Details, name='County_Details'),
    path('edit_dish/<int:pk>',views.edit_dish, name='edit_dish'),
    path("checkout/", views.checkout, name="Checkout"),
    path("About_Us/", views.About_Us, name="About_Us"),
    path("Contact_Us/", views.Contact_Us, name="Contact_Us"),
    path("Devlopers/", views.Devlopers, name="Devlopers"),
    path("order_confirm/", views.order_confirm, name="order_confirm"),
    url(r'^veg/(?P<pk>\d)/$', views.veg, name="vegetarian"),
    url(r'^non-veg/(?P<pk>\d)/$', views.non_veg, name="non-vegetarian"),
    url(r'^chinese/(?P<pk>\d)/$', views.chinese, name="chinese"),
    url(r'^italian/(?P<pk>\d)/$', views.italian, name="italian"),
    #path("password_change/", views.password_change, name="password_change"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]