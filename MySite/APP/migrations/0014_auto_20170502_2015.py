# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0013_auto_20170429_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='grade',
            new_name='grades',
        ),
    ]