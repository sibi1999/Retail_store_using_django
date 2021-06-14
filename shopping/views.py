from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from shopping.models import Item,OrderItem,ConfirmedTicket
from django.db.models import Sum
from django.views.generic import ListView,DetailView,View
from django.contrib import messages
import datetime
# Create your views here.

id=0


def test(request):
    return render(request,'shopping/index.html')
class HomeView(ListView):
    model=Item 
    template_name="shopping/home-page.html"
    paginate_by = 4




class ItemDetailView(DetailView):
    model=Item 
    template_name="shopping/product-page.html"


def add_to_cart(request,pk):
    global id
    id=id+1
    print(id)
    
    try:
        item=get_object_or_404(Item,pk=pk)
        cart=OrderItem()
        cart.id=id
        cart.item=item
        cart.user=request.user
        cart.quantity=1
        if cart.item.discount_price:
            cart.sub_total= cart.item.discount_price * cart.quantity    
        else:
            cart.sub_total= cart.item.price * cart.quantity  

        cart.ordered= False
        cart.save()

    except:
        pass
    messages.info(request, 'Product Added to cart successfully')
    return redirect('shopping:home')


def cart(request):

    all_items=OrderItem.objects.all()
    overall_sum=all_items.aggregate(Sum('sub_total'))['sub_total__sum']
    
    return render(request,'shopping/mycart.html',{'data':all_items,'total':overall_sum})




def inc(request,pk):
    cp_obj = OrderItem.objects.get(id=pk)
    cp_obj.quantity += 1
    if cp_obj.item.discount_price:
            cp_obj.sub_total= cp_obj.item.discount_price * cp_obj.quantity    
    else:
        cp_obj.sub_total= cp_obj.item.price * cp_obj.quantity  
    cp_obj.save()
    all_items=OrderItem.objects.all()
    overall_sum=all_items.aggregate(Sum('sub_total'))['sub_total__sum']
    return render(request,'shopping/mycart.html',{'data':all_items,'total':overall_sum})


def dcr(request,pk):
    cp_obj = OrderItem.objects.get(id=pk)
    cp_obj.quantity -= 1
    if cp_obj.item.discount_price:
            cp_obj.sub_total= cp_obj.item.discount_price * cp_obj.quantity    
    else:
        cp_obj.sub_total= cp_obj.item.price * cp_obj.quantity  
    cp_obj.save()
    all_items=OrderItem.objects.all()
    overall_sum=all_items.aggregate(Sum('sub_total'))['sub_total__sum']
    return render(request,'shopping/mycart.html',{'data':all_items,'total':overall_sum})


def rmv(request,pk):
    cp_obj = OrderItem.objects.get(id=pk)
    cp_obj.delete()
    
    all_items=OrderItem.objects.all()
    overall_sum=all_items.aggregate(Sum('sub_total'))['sub_total__sum']
    return render(request,'shopping/mycart.html',{'data':all_items,'total':overall_sum})
    




'''
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order-summary")


'''
   




def checkout(request):
    all_items=OrderItem.objects.all()
    overall_sum=all_items.aggregate(Sum('sub_total'))['sub_total__sum']
    return render(request,'shopping/checkout-page.html',{'data':all_items,'total':overall_sum})
    



def order(request):
    #ticket=ConfirmedTicket()
    name=request.POST.get('firstName')+request.POST.get('lastName')
    email=request.POST.get('email')
    address=request.POST.get('address')
    country=request.POST.get('country')
    state=request.POST.get('state')
    zip=request.POST.get('zip')
    all_items=OrderItem.objects.all()
    
    for i in all_items:
        ticket=ConfirmedTicket()
        try:
            ticket.id=ConfirmedTicket.objects.all()[-1].id+1
        except:
            ticket.id=i.id
        ticket.name=name 
        ticket.user=i.user
        ticket.email=email  
        ticket.address=address 
        ticket.state=state 
        ticket.zip=zip
        ticket.product_name=i.item.title 
        ticket.product_price=i.sub_total 
        ticket.quantity=i.quantity 
        ticket.date = datetime.datetime.now()
        ticket.save()
    all_items.delete()

    # ticket.name=
    # ticket.email=email

    print(name)
    print(request.POST)



    print("\n"*10)
    print(request.POST['address'])
            
    return redirect('shopping:home')
        

