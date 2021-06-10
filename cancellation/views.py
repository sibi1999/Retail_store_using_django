from django.shortcuts import render
from django import forms

# Create your views here.


from django import forms

class CancellationForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

def cancellation_view(request):
    if request.method == 'POST':
        cancel = CancellationForm(request.POST)    
        if cancel.is_valid():
            name = cancel.cleaned_data['name']
            print(name, '\n'*100)

    cancel = CancellationForm()
    
    return render(request, 'cancellation/cancel.html', {'form': cancel})