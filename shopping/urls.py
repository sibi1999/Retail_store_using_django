from django.urls import path

from django.conf.urls.static import  static
from .views import (
    HomeView,ItemDetailView,order,add_to_cart,cart,ManageCartView
)
app_name='shopping'
urlpatterns = [
     path('',HomeView.as_view(),name="home"),
     path('checkout/<int:pk>/',ItemDetailView.as_view(),name="item_view"),
   
    
#    # path('checkout',checkout,name="checkout"),
    path('product',order,name="order"),
    path('add-to-cart/<int:pk>',add_to_cart,name="add-to-cart"),
    path('cart',cart,name='cart'),
    path("manage-cart/<slug>/", ManageCartView.as_view(), name="managecart")
]