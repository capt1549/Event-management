from unicodedata import name
from app.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home',INDEX,name="home"),
    path('add',Add,name='add'),
    path('edit',Edit,name='edit'),
    path('update/<str:id>',Update,name='update'),
    path('delete/<str:id>',Delete,name='delete'),
    path('',signin,name="signin"),
    path('signupadmin',signupadmin,name="signupadmin"),
    path('loginuser',loginuser,name="loginuser"),
    path('signout',signout,name='signout'),
    path('user',user,name='user'),
    path('admin_login',admin_login,name='admin_login'),
    path('loginadmin',loginadmin,name='loginadmin'),
    path('signupuser',signupuser,name='signupuser'),
    path('admin_signup',admin_signup,name='admin_signup'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)