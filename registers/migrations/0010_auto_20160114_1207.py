# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 04:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0009_auto_20160112_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='url',
            field=models.CharField(blank=True, help_text='URL to webpage with more information', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='mtd',
            field=models.DurationField(default=datetime.timedelta(14), help_text='Maximum Tolerable Downtime (days hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='process',
            name='rpo',
            field=models.DurationField(default=datetime.timedelta(1), help_text='Recovery Point Objective/Data Loss Interval (days hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='process',
            name='rto',
            field=models.DurationField(default=datetime.timedelta(7), help_text='Recovery Time Objective (days hh:mm:ss)'),
        ),
    ]
