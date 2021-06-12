from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from shopping.models import Item,OrderItem
from django.db.models import Sum
from django.views.generic import ListView,DetailView,View
# Create your views here.

id=0

class HomeView(ListView):
    model=Item 
    template_name="shopping/home-page.html"


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
    return render(request,'shopping/product-page.html')


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
    return render(request,'shopping/product-page.html')

