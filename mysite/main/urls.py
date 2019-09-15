from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import dish_detail_view


urlpatterns=[
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login.url"),
    path('dishlist/',views.dish_list_view,name="dishlist"),
    path('signup/',views.registerView,name="signup"),
    path('dishdetail/',views.dish_detail_view,name='dishdetail'),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
   
]