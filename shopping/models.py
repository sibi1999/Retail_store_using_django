from django.db import models

# Create your models here.

category_choices=[('S','SHIRT'),('SW','SHIRT WEAR'),('OW','OUT WEAR')]
label_choices=[('P','primary'),('S','secondary'),('D','danger')]
class item(models.Model):
    '''name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=200)
    '''
    
    title=models.CharField(max_length=100)
    price=models.FloatField()
    category=models.CharField(choices=category_choices,max_length=2)
    label=models.CharField(choices=label_choices,max_length=2)

    