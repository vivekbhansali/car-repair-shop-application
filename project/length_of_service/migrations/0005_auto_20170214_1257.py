# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('length_of_service', '0004_auto_20170214_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairtypes',
            name='national_averages',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
