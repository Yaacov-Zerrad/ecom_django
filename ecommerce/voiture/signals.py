import uuid
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from achetteur.models import Buyers
from voiture.models import Cars


# @receiver(pre_save, sender=Cars)
# def pre_save_create_code(sender, instance, **kwargs):
#     if instance.code == "":
#         instance.code = str(uuid.uuid4()).replace('-','').upper()[:10]
    
#     #relation buyer voiture si choisi une voitur (le rendre actif)
#     obj = Buyers.objects.get(user=instance.buyer.user)
#     obj.actif = True
#     obj.save()
  
  
  
# .save() obligtoir dans post
@receiver(post_save, sender=Cars)
def post_save_create_code(sender, instance, created,  **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace('-','').upper()[:10]
        instance.save()
    #relation buyer voiture si choisi une voitur (le rendre actif)
    obj = Buyers.objects.get(user=instance.buyer.user)
    obj.actif = True
    obj.save()
     
 # DIFF ENTRE POST PRE ET SAVE
 # save = si le champ a modifier ne depand pas d une autre aplication 
 # post = si le champ a modifier  depand d une autre aplication 
 # egalement pour pre mais post est preferable
 #
     
     
     
     
     