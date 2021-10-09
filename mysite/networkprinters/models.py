# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from typing import Text, Tuple
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.db.models.query import FlatValuesListIterable

from django.utils import tree
from psycopg2.extensions import TRANSACTION_STATUS_ACTIVE, TRANSACTION_STATUS_UNKNOWN
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.IntegerField(null=True,blank=True)
    mail_id = models.EmailField(max_length=200,null=True,blank=True)
    college = models.CharField(max_length=100,null=True,blank=True)
    designation = models.CharField(max_length=100,blank=True,null=True)
  
    
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(getattr(self,field.attname,''))
        return ':'.join(map(str,field_values))
    

    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile is Created")
        
#post_save.connect(create_profile,sender=User)

@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created == False:
        instance.profile.save()
        print("Profile Updated")
    
#post_save.connect(update_profile,sender=User)

    
    
class FeedbackForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,null=True,default="")
    company = models.CharField(max_length=300,null=True,default="")
    designation = models.CharField(max_length=300,null=True,default="")
    email = models.EmailField(max_length=300,null=True,default="")
    feedback = models.CharField(max_length=600,null=True,default="")
    
    def __str__(self):
        return self.name
