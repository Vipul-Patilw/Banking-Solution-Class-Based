#pylint:disable=E0001
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .views import changePassword
from .views import GoToLogin
from bankingSolution.uservarification_view import  uservarification
urlpatterns = [
	path('user/', include('django.contrib.auth.urls')),
	path('user-verification', uservarification.UserVerification.as_view(), name='userverification'),
   path('sign',views.index, name='sign'),
   path('logininfo.html',views.index, name='sign'),
   path('home',views.home, name='home'),
   path('login',views.sign, name='login'),
   path('index.html',views.sign, name='login'),
   path('home',views.home, name='home'),
   path('home',views.home, name='home'),
   path('chat',views.chat, name='chat'),
   path('balance',views.balance, name='balance'),
   path('balance2.html',views.balance, name='balance'),
   path('setting.html',views.setting, name='setting'),
   path('balance copy 4.html',views.sendMoney, name='sendMoney'),
   path('send',views.sendMoney, name='sendMoney'),
   path('recharge',views.recharge, name='rechargeplan'),
   path('changePin.html',views.changePin, name='changePin'),
   path('recharge.html',views.recharge, name='rechargeplan'),
   path('operator.html',views.operator, name='operator'),
   path('about.html',views.about, name='about'),
   path('',views.lock, name='lock'),
   path('lock',views.lock, name='lock'),
   path('lock2',views.lock2, name='lock'),
   path('lock2.html',views.lock, name='lock'),
   path('lock.html',views.lock2, name='lock'),
   path('fgdf.html',views.privacy, name='privacyPolicy'),
   path('pass.html',changePassword.as_view(template_name='changePassword.html')),
 #  path('set',changePassword.as_view(template_name='resatePassword.html')),
   path('password_success',views.password_success, name='password_success'),
   path('ddd.html',views.personalDetails, name='personalDetails'),
   path('bank',views.bankDetails, name='bankDetails'),
   path('BankDetailsNotice.html-<email1>',views.bankDetails2, name='bankDetails'),
   path('moneyrecived-<account_number>-<date>',views.moneyrecived, name='money'),
   path('BankDetails2.html',views.bankDetails, name='bankDetails'),
   path('BankDetailsEdit.html',views.bankDetailsEdit, name='bankDetails'),
   path('withdraw.html',views.withdraw, name='withdraw'),
   path('logout',views.logoutuser, name='logout'),
   path('map.html',views.map, name='map'),
   path('gotologin.html',GoToLogin.as_view(), name='gotologin'),
   path('activate/<uidb64>/<token>',views.activate, name='activate'),
#   path('forgotPassword.html',views.forgotPassword, name='forgotPassword'),
   
   path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   
   path('password_reset/ done/', auth_views. PasswordResetDoneView. as_view(), name='password_ reset_done'),
   
   path('reset/<uidb64>/<token>/ ', auth_views.PasswordResetConfirmView.as_view, name='password_reset_confirm'),
   
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name=' password_reset_complete')

]




