from django.db import models

# Create your models here.

from django.shortcuts import reverse
from django.conf import settings
# Create your models here.

category_choices=[('S','SHIRT'),('SW','SPORT WEAR'),('OW','OUT WEAR')]
label_choices=[('P','primary'),('S','secondary'),('D','danger')]
class Item(models.Model):
    '''name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=200)
    '''
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=category_choices,max_length=2)
    label=models.CharField(choices=label_choices,max_length=2)
    slug=models.SlugField()
    description= models.TextField()
    img_url=models.CharField(max_length=1000)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("shopping:item_view",kwargs={'pk':self.id})

    def get_add_to_cart(self):
        return reverse("shopping:add-to-cart",kwargs={'pk':self.id})
        

class OrderItem(models.Model):

    id = models.IntegerField(primary_key=True,unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    sub_total=models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.item.title} by {self.user}"


class ConfirmedTicket(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    country=models.CharField(max_length=1000)
    state=models.CharField(max_length=1000)
    zip=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000,default="a")
    product_name=models.CharField(max_length=1000)
    product_price= models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product_name} by {self.user}"

    



    