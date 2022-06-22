from tkinter import CASCADE
from django.db import models
from commande.models import Orders


class Sales(models.Model):
    order= models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.amount)
    
