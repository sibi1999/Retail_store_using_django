from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.

def signup_view(request):
    
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            print("hghg")
            user=form.save()
           
            #print(data['username'])
            login(request,user)
            return redirect('shopping:home')
    else:
        form=UserCreationForm()
    return render(request,'signup/index.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            print(form)
            print("login successfully")
            return redirect('shopping:home')#next page
    else:
        form=AuthenticationForm()
    return render(request,'login/index.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        # return render(request,'login/index2.html')
        return redirect('accounts:login')

