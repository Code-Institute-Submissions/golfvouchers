# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-15 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200415_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='manufacturer',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
