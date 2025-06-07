from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Location,Profile

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,*args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=Profile)
def create_user_location(sender,instance,created,*args, **kwargs):
    if created:
        profile_location=Location.objects.create()
        instance.location=profile_location
        instance.save()

@receiver(post_delete,sender=Profile)
def delete_user_location(sender,instance,created,*args, **kwargs):
    if instance.location:
        instance.location.delete()