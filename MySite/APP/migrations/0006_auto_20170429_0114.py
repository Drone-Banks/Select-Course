# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_auto_20170429_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='select',
            name='sid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='APP.Student'),
            preserve_default=False,
        ),
    ]