# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bootswatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cerulean', 'Cerulean'), ('Cosmo', 'Cosmo'), ('Cyborg', 'Cyborg'), ('Darkly', 'Darkly'), ('Flatly', 'Flatly'), ('Journal', 'Journal'), ('Lumen', 'Lumen'), ('Paper', 'Paper'), ('Readable', 'Readable'), ('Sandstone', 'Sandstone'), ('Simplex', 'Simplex'), ('Slate', 'Slate'), ('Spacelab', 'Spacelab'), ('Superhero', 'Superhero'), ('United', 'United'), ('Yeti', 'Yeti')], default='Flatly', max_length=15)),
            ],
            options={
                'verbose_name': 'Swatch',
                'verbose_name_plural': 'Swatch',
            },
        ),
    ]
