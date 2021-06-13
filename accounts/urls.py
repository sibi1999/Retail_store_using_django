from django.urls import path
from . import views
from django.conf.urls.static import  static

app_name='mysite'

urlpatterns = [
   
    path('s/',views.signup_view,name='signup'),
    path('',views.login_view,name='login'),
    path('lo/',views.logout_view,name='logout')]