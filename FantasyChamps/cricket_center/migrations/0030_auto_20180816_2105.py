# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-16 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_center', '0029_auto_20180814_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Captain',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Vice_Captain',
            field=models.CharField(default='', max_length=255),
        ),
    ]
