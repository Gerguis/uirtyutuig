# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_center', '0005_auto_20180729_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchdetails',
            name='match_date',
            field=models.DateTimeField(default=1532849743.3128803),
        ),
    ]
