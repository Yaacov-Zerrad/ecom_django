import uuid
from django.db import models
from achetteur.models import Buyers

class Cars(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    # en fonction du connecter
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    
    
    # def save(self, *args, **kwargs):
    #     if self.code == "":
    #         self.code = str(uuid.uuid4()).replace('-','').upper()[:10]
    #     return super().save(*args, **kwargs)
