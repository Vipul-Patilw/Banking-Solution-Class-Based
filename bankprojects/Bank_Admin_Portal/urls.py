from django.contrib import admin
from django.urls import path,include
from . import  views
from Bank_Admin_Portal.registration_view import superusercreate
from Bank_Admin_Portal.userscreation_view import  usercreation_view
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('superuser/', include('django.contrib.auth.urls')),
#	path('superuser/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('superuser/create',superusercreate.SuperUserCreate.as_view(),name='admin'),
    path('user/account-create',views.UserAccountCreate.as_view(),name='useraccount'),
    path('home',views.UsersDetail.as_view(),name='home'),
    path('',views.UsersDetail.as_view(),name='home')
   ]
   
LOGIN_REDIRECT_URL = '/users-detail'
LOGOUT_REDIRECT_URL = 'bankpay-admin/superuser/login'