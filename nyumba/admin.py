from django.contrib import admin
from .models import Profile, NeighbourHood, JoinHood, Business, Allert, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(JoinHood)
admin.site.register(Business)
admin.site.register(Allert)
admin.site.register(Comment)
