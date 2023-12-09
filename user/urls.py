
from django.contrib import admin
from django.urls import path
from user import views
app_name="user"

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('user_logout',views.user_logout,name="user_logout"),
]
