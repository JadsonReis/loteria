# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 00:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0003_auto_20160603_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concursos',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 6, 3, 0, 32, 50, 16392)),
        ),
    ]