# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20161101_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='website1',
            new_name='website',
        ),
    ]
