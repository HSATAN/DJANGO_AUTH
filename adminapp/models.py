# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=16)
    last_login = models.DateTimeField(null=True, blank=True,auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'admin_user'

    def is_authenticated(self, **kwargs):
        return True