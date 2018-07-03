# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=30)
    epwd = models.CharField(max_length=50)

    def __unicode__(self):
        return u'Employee:%s'%self.ename