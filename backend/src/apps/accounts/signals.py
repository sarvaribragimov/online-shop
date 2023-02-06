from django.db.models.signals import post_save
from .models import Account,UserProfile
from django.dispatch import receiver
# post_save bazaga saqlab bulgandan sung ishga tushadi
# pre_save - bazaga saqlashidan oldin ishga tushadi
@receiver(post_save,sender=Account)
def create_user(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
