# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0009_auto_20170429_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='select',
            name='cid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='APP.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='select',
            name='sid',
            field=models.ManyToManyField(to='APP.Student'),
        ),
    ]
