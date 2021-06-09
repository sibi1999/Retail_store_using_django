from django.urls import path
from . import views
from django.conf.urls.static import  static

urlpatterns = [
    path('', views.home,name="home"),
    path('checkout',views.checkout,name="checkout"),
    path('product',views.order,name="order")
]