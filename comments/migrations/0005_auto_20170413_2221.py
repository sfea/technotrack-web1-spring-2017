# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 22:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20170413_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 14, 4, 21, 39, 911119)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 14, 1, 21, 39, 911208)),
        ),
    ]
