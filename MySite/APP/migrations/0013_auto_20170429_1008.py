# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0012_auto_20170429_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=0),
        ),
    ]
