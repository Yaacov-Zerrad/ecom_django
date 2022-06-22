from .models import Sales
from django.dispatch import receiver
from django.db.models.signals import pre_delete

@receiver(pre_delete, sender=Sales)
def pre_delete_orders(sender, instance,  **kwarg):
    obj = instance.order
    obj.activate = False
    obj.save()