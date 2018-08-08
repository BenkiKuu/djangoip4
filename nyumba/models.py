from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    neighbourhood_location = models.CharField(max_length =250)
    population_count = models.IntegerField(null=True)
    admin = models.ForeignKey(User)

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search_neighbourhood(cls,search_term):
        neighbourhood = cls.objects.filter(name__icontains = search_term)
        return neighbourhood

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User)
    location = models.ForeignKey(NeighbourHood, null=True)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    business_logo = models.ImageField(upload_to='images/')
    business_moto = models.CharField(max_length=300)
    user = models.OneToOneField(User)
    hood = models.ForeignKey(NeighbourHood, null=True)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(name__icontains = search_term)
        return business

class JoinHood(models.Model):
   user_id = models.OneToOneField(User)
   hood_id = models.ForeignKey(NeighbourHood)

   def __str__(self):
       return self.user_id

class Allert(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    user = models.ForeignKey(User)
    hood = models.ForeignKey(NeighbourHood)

    def __str__(self):
        return self.title

    def save_allert(self):
        self.save()

    def delete_allert(self):
        self.delete()


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Allert)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
