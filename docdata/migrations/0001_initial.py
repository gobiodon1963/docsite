# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apl_id', models.CharField(max_length=20, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442')),
                ('inn', models.CharField(max_length=50, verbose_name='\u0418\u041d\u041d')),
                ('kpp', models.CharField(max_length=9, verbose_name='\u041a\u041f\u041f')),
                ('address', models.CharField(max_length=250, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('need_to_import', models.BooleanField(default=False, verbose_name='\u041d\u0443\u0436\u0435\u043d \u0438\u043c\u043f\u043e\u0440\u0442')),
            ],
        ),
        migrations.CreateModel(
            name='DocHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(max_length=40, verbose_name='\u0422\u0438\u043f')),
                ('doc_number', models.CharField(max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440')),
                ('doc_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('apl_name', models.CharField(max_length=250, verbose_name='\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442')),
                ('apl_inn', models.CharField(max_length=50, verbose_name='\u0418\u041d\u041d')),
                ('apl_kpp', models.CharField(max_length=9, verbose_name='\u041a\u041f\u041f')),
                ('apl_address', models.CharField(max_length=250, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('stock', models.CharField(max_length=50, verbose_name='\u0421\u043a\u043b\u0430\u0434')),
                ('account', models.CharField(max_length=20, verbose_name='\u0420/\u0441\u0447\u0435\u0442')),
                ('currency', models.CharField(max_length=3, verbose_name='\u0412\u0430\u043b')),
                ('total_sum', models.FloatField(verbose_name='\u0421\u0443\u043c\u043c\u0430')),
                ('pp_number', models.CharField(blank=True, max_length=10, verbose_name='\u2116 \u043f\\\u043f')),
                ('sf_number', models.CharField(blank=True, max_length=10, verbose_name='\u2116 \u0441-\u0444')),
            ],
        ),
        migrations.CreateModel(
            name='DocTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.CharField(max_length=20, verbose_name='\u0410\u0440\u0442\u0438\u043a\u0443\u043b')),
                ('name', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('unit_id', models.CharField(max_length=10, verbose_name='\u0435\u0434.')),
                ('unit_code', models.CharField(max_length=3, verbose_name='\u041a\u043e\u0434')),
                ('qty', models.FloatField(default=1, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('item_sum', models.FloatField(verbose_name='\u0421\u0443\u043c\u043c\u0430')),
                ('width', models.IntegerField(verbose_name='\u0428\u0438\u0440\u0438\u043d\u0430')),
                ('height', models.IntegerField(verbose_name='\u0412\u044b\u0441\u043e\u0442\u0430')),
                ('gtd', models.CharField(max_length=30, verbose_name='\u0413\u0422\u0414')),
                ('country_code', models.CharField(max_length=2, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docdata.DocHeader', verbose_name='\u2116 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.CharField(max_length=20, verbose_name='\u0410\u0440\u0442\u0438\u043a\u0443\u043b')),
                ('name', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('full_name', models.CharField(default=b'', max_length=1024, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('unit_id', models.CharField(max_length=10, verbose_name='\u0435\u0434.')),
                ('unit_code', models.CharField(max_length=3, verbose_name='\u041a\u043e\u0434')),
                ('need_to_import', models.BooleanField(default=False, verbose_name='\u041d\u0443\u0436\u0435\u043d \u0438\u043c\u043f\u043e\u0440\u0442')),
            ],
        ),
    ]
