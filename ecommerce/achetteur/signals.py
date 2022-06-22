from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyers

# sender = qui qui donne les donnees
@receiver(post_save, sender=User)
def post_save_create_buyers(sender, instance, created, **kwargs):
    if created:
        Buyers.objects.create(user=instance)