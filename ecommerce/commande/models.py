from django.db import models
from voiture.models import Cars

class Orders(models.Model):
    name = models.CharField(max_length=20)
    cars = models.ManyToManyField(Cars)
    qte = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    activate = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
    
