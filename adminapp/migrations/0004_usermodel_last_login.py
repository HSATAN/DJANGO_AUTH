# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_auto_20170818_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
