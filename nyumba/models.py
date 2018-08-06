from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Business.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.business.save()


class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField(max_length =60)
    neighbourhoo_location = CharField(max_length =250)
    ocupants_count = models.IntergerField()
    admin = models.ForeignKey(User)


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User)
    location = models.ForeignKey(NeighbourHood, null=True)
    email = models.EmailField((null = True)

class Business(models.Model):
    business_logo = models.ImageField(upload_to='images/')
    business_moto = models.CharField(max_length=300)
    user = models.OneToOneField(User)
    location = models.ForeignKey(NeighbourHood, null=True)
    email = models.EmailField(null = True)
