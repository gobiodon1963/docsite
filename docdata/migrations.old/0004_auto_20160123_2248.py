# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docdata', '0003_auto_20160123_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docheader',
            name='pp_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='docheader',
            name='total_sum',
            field=models.FloatField(),
        ),
    ]
