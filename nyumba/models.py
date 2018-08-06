from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField




class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField(max_length =60)
    neighbourhoo_location = CharField(max_length =250)
    ocupants_count = models.IntergerField()
    admin = models.ForeignKey(User)
