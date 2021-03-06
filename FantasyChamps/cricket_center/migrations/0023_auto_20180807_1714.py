# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_center', '0022_auto_20180807_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat1',
            new_name='Player10',
        ),
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat2',
            new_name='Player11',
        ),
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat3',
            new_name='Player2',
        ),
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat4',
            new_name='Player3',
        ),
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat5',
            new_name='Player4',
        ),
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat6',
            new_name='Player5',
        ),
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat7',
            new_name='Player6',
        ),
        migrations.RenameField(
            model_name='indiapakistanteam',
            old_name='Bat8',
            new_name='Player7',
        ),
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Player8',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Player9',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
    ]
