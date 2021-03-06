# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_center', '0020_auto_20180806_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Bat1',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Bat2',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Bat3',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Bat4',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
        migrations.AddField(
            model_name='indiapakistanteam',
            name='Bat5',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
        migrations.AlterField(
            model_name='indiapakistanteam',
            name='Keeper',
            field=models.CharField(default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}", max_length=255),
        ),
    ]
