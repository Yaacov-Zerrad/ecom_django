from ast import Return
from django.db import models
from django.forms import CharField
from django.urls import reverse

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address =models.CharField(max_length=200)
    skill = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)
    langue = models.CharField(max_length=500)
    interest= models.CharField(max_length=1000)
    experience = models.TextField()
    education = models.TextField()
    project = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("verification", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['-date_added']





