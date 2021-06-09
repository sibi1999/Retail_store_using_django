from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'shopping/home-page.html')

def checkout(request):
    return render(request,'shopping/checkout-page.html')

def order(request):
    return render(request,'shopping/product-page.html')

