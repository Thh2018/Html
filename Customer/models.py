# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CustomerCondition(models.Model):
    condition_id = models.AutoField(primary_key=True)
    condition_name = models.CharField(max_length=50, blank=True, null=True)
    condition_explain = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)




class CustomerSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)




class CustomerType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)


