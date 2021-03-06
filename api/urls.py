from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[
    path('reg' , views.regUser,  name='reg'),
    path('' ,views.home , name='home'),
    path('login' , views.loginUser, name='login'),
    path('profile', views.userProfile, name='profile'),
    path('sites', views.api,  name='sites'),
    path('submit-site',views.submit_site, name='submit-site'),
    path('site/<int:id>/', views.ReviewView , name='site_details'),
    path('results', views.search_project, name='results'),


    # path('logout', auth_views.LogoutView.as_view(template_name="api/logout.html"), name='logout'),
    path('logout', views.logoutUser, name='logout')

]