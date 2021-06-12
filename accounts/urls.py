from django.urls import path
from . import views
from django.conf.urls.static import  static

app_name='mysite'

urlpatterns = [
    path('',views.login_view,name='test'),
    path('s/',views.signup_view,name='signup'),
    path('lo/',views.logout_view,name='logout')]