from django.db import models

# Create your models here.

from django.shortcuts import reverse
from django.conf import settings
# Create your models here.

category_choices=[('S','SHIRT'),('SW','SHIRT WEAR'),('OW','OUT WEAR')]
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


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("shopping:item_view",kwargs={'pk':self.id})

    def get_add_to_cart(self):
        return reverse("shopping:add-to-cart",kwargs={'pk':self.id})
        

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return f"{self.item.title} by {self.user}"


    