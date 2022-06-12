from django.urls import path
from .views import SiteDetailView
from . import views

urlpatterns=[
    path('' , views.regUser,  name='reg'),
    path('home' ,views.home , name='home'),
    path('login' , views.loginUser, name='login'),
    path('profile', views.userProfile, name='profile'),
    path('sites', views.api,  name='sites'),
    path('submit-site',views.submit_site, name='submit-site'),
    path('site/<int:pk>/', SiteDetailView.as_view() , name='site_details')
]