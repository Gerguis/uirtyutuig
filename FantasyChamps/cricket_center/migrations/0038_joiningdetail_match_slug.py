# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_center', '0037_joiningdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='joiningdetail',
            name='match_slug',
            field=models.CharField(default='', max_length=255),
        ),
    ]