# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 05:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0016_auto_20160509_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentuser',
            name='account_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Dept fixed-term contrac'), (1, 'N/A'), (2, 'Permanent'), (3, 'Recruitment agency contract'), (4, 'Resigned'), (5, 'Shared account'), (6, 'Vendor'), (7, 'Volunteer')], null=True),
        ),
        migrations.AddField(
            model_name='departmentuser',
            name='alesco_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Readonly data from Alesco', null=True),
        ),
    ]
