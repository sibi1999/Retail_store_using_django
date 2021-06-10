from django.db import models
from django.db.models.base import Model

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    