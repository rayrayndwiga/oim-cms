# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-18 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0016_auto_20160316_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processitsystemrelationship',
            old_name='criticality',
            new_name='importance'
        ),
        migrations.AlterField(
            model_name='itsystem',
            name='schema_url',
            field=models.URLField(blank=True, help_text='URL to schema diagram', max_length=2000, null=True),
        ),
    ]
