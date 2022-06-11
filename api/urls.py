from django.urls import path
from . import views

urlpatterns=[
    path('' , views.regUser,  name='api-reg'),
    path('home' ,views.home , name='home'),
    path('login' , views.loginUser, name='login'),
    path('profile', views.userProfile, name='profile')
]