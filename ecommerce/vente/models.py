from tkinter import CASCADE
from django.db import models
from commande.models import Orders


class Sales(models.Model):
    order= models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.amount)
    
    
    
# on fait un news manager
class ProductManager(models.Manager):
    def get_queryset(self, *args,  **kwargs) :
        return super().get_queryset(*args, **kwargs)
    
    
class Product(models.Model):
    product = ProductManager()
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name
    