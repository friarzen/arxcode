# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0006_auto_20181202_2018'),
        ('exploration', '0052_auto_20181123_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShardhavenAffinityChance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(default=10)),
                ('affinity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='magic.Affinity')),
                ('haven', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affinity_chances', to='exploration.Shardhaven')),
            ],
        ),
        migrations.CreateModel(
            name='ShardhavenAlignmentChance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(default=10)),
                ('alignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='magic.Alignment')),
                ('haven', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alignment_chances', to='exploration.Shardhaven')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='shardhavenalignmentchance',
            unique_together=set([('haven', 'alignment')]),
        ),
        migrations.AlterUniqueTogether(
            name='shardhavenaffinitychance',
            unique_together=set([('haven', 'affinity')]),
        ),
    ]
