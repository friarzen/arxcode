# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-07 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0002_auto_20180722_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokeredsale',
            name='broker_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Purchase'), (0, 'Sale')], default=0),
        ),
    ]
