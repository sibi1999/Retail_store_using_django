from django.urls import path

from django.conf.urls.static import  static
from .views import (
    HomeView,ItemDetailView,order,add_to_cart,cart,inc,dcr,rmv,checkout,test
)
app_name='shopping'
urlpatterns = [
     path('',HomeView.as_view(),name="home"),
     path('product/<int:pk>/',ItemDetailView.as_view(),name="item_view"),
     path('order/',order,name='order'),
     path('test/',test,name='test'),
    
    path('checkout',checkout,name="checkout"),
    #path('product',order,name="order"),
    path('add-to-cart/<int:pk>',add_to_cart,name="add-to-cart"),
    path('cart',cart,name='cart'),
    path("inc/<int:pk>/", inc, name="inc"),
    path("dcr/<int:pk>/", dcr, name="dcr"),
    path("rmv/<int:pk>/", rmv, name="rmv")
    
]