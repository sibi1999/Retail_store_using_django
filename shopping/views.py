from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from shopping.models import Item,OrderItem
from django.views.generic import ListView,DetailView,View
# Create your views here.



class HomeView(ListView):
    model=Item 
    template_name="shopping/home-page.html"


class ItemDetailView(DetailView):
    model=Item 
    template_name="shopping/product-page.html"


def add_to_cart(request,pk):
    item=get_object_or_404(Item,pk=pk)
    cart=OrderItem()
 
    cart.item=item
    cart.user=request.user
    cart.quantity=1 
    cart.ordered= False
    cart.save()
    return render(request,'shopping/product-page.html')


def cart(request):
    print("hi","\n"*10)

    all_items=OrderItem.objects.all()
    print("all",all_items)
    return render(request,'shopping/mycart.html',{'data':all_items})



class ManageCartView(View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        action = request.GET.get("action")
        cp_obj = OrderItem.objects.all().filter(item__slug=slug)
        
    


        if action == "inc":
            cp_obj.quantity += 1
            #cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            #cart_obj.total += cp_obj.rate
            cart_obj.save()
        '''
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()

        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect("ecomapp:mycart")



'''







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
   



'''
def checkout(request):
    return render(request,'shopping/checkout-page.html')


'''
def order(request):
    return render(request,'shopping/product-page.html')

