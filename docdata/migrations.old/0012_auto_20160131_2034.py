# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docdata', '0011_product_need_to_import'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='need_to_import',
            field=models.BooleanField(default=False, verbose_name='Нужен импорт'),
        ),
    ]