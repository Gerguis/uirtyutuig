# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_center', '0038_joiningdetail_match_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joiningdetail',
            old_name='joined_contest',
            new_name='joined_contest_slug',
        ),
    ]
