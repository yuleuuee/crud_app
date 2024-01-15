from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name ='home'),

    path('login/',views.user_login,name ='login'), # "name : login "--> is the same as  <a href="{% url 'login' %}"> in the home page
    # path('signup/',views.user_signup,name ='signup'),
    path('profile/',views.user_profile,name ='profile'),
    path('logout/',views.user_logout,name ='logout'),
    
]