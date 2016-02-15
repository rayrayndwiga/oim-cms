# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0007_location_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('function', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='registers.Function')),
            ],
        ),
        migrations.AddField(
            model_name='itsystem',
            name='function',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='registers.Function'),
        ),
        migrations.AddField(
            model_name='itsystem',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='registers.Process'),
        ),
    ]