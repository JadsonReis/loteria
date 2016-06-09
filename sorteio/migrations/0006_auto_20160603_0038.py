# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 00:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio', '0005_auto_20160603_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concursos',
            name='acumulado',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='concursos',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 6, 3, 0, 38, 18, 58479)),
        ),
        migrations.AlterField(
            model_name='concursos',
            name='gan_quadra',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='concursos',
            name='gan_quina',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='concursos',
            name='gan_sena',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
