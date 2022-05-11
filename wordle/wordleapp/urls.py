from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('token/', obtain_auth_token),
    path('signup/', views.signup),
    
]
