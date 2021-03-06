# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4

def make_uuid():
   """Return UUID4 string."""
   return str(uuid4())

class UUIDModel(models.Model):
   uuid = models.CharField(primary_key=True,
      editable=False, max_length=36, db_index=True, default=make_uuid)

   class Meta:
      abstract = True

class Location(models.Model):
    objects = models.Manager()
    coordinates = models.CharField(primary_key=True ,max_length=64 ,editable=False, null = False)
    address = models.CharField(max_length=256, null=True , blank = True)

class RestaurantModel(UUIDModel):
   objects = models.Manager()
   restaurant_name = models.CharField(max_length=256, null=True, blank = True) 
   restaurant_type = models.CharField(max_length=256, null=True , blank = True)
   phone = models.CharField(max_length=256, null = True, blank = True)
   location = models.OneToOneField(Location, on_delete=models.CASCADE, null = True, blank = True)