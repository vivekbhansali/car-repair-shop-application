# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepairTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_type', models.CharField(max_length=1)),
                ('description', models.CharField(max_length=30)),
                ('national_averages', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'repair_types',
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropoff', models.DateField()),
                ('pickup', models.DateField()),
                ('mechanic', models.CharField(max_length=30)),
                ('repair_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='length_of_service.RepairTypes')),
            ],
            options={
                'db_table': 'shop_workflow_fact',
            },
        ),
    ]
