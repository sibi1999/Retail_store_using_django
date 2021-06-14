from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from shopping.models import ConfirmedTicket 

# Create your views here.


from django import forms

class CancellationForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)


def cancellation_view(request):
    # if request.method == 'POST':
    #     cancel = CancellationForm(request.POST)    
    #     if cancel.is_valid():
    #         name = cancel.cleaned_data['name']
    #         p = models.Product()
    #         p.title = name
    #         p.save()

    # cancel = CancellationForm()
    user = request.user
    orderedProducts = ConfirmedTicket.objects.filter(user_id = user.id)

    
    return render(request, 'cancellation/cancel.html', {'form': cancel, 'orderedProducts': orderedProducts})

def cancel(request, slug):
    orderedProducts = ConfirmedTicket.objects.all()
    user = request.user
    d = ConfirmedTicket.objects.filter(product_name = slug, user_id = user.id)[0].delete()
    return redirect('cancellation:cancellation')