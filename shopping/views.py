from django.shortcuts import render
from django.http import HttpResponse
from shopping.models import item
# Create your views here.

def home(request):
    key=item.objects.all()
    return render(request,'shopping/home-page.html',{'data':key})

def checkout(request):
    return render(request,'shopping/checkout-page.html')

def order(request):
    return render(request,'shopping/product-page.html')

