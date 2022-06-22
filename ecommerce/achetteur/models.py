from django.db import models
from django.contrib.auth.models import User


# lor de la creation de user ca cree aussi ca
class Buyers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    actif = models.BooleanField(default=False)
    
    def __str__(self) :
        return str(self.user)