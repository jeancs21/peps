# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-11 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adopcion', '0003_auto_20180611_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudadopcion',
            name='fecha',
            field=models.DateField(),
        ),
    ]
