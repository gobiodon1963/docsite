# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docdata', '0002_auto_20160123_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docheader',
            name='sf_number',
            field=models.CharField(max_length=10),
        ),
    ]