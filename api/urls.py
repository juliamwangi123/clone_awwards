from django.urls import path
from . import views

urlpatterns=[
    path('' , views.regUser,  name='api-reg'),
    path('home' ,views.home , name='home')
]