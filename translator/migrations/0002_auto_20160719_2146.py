# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translator',
            name='langs',
        ),
        migrations.AddField(
            model_name='translator',
            name='from_langs',
            field=models.CharField(default='English,Polish,German,Spanish', max_length=100),
        ),
        migrations.AddField(
            model_name='translator',
            name='to_langs',
            field=models.CharField(default='English,Polish,German,Spanish', max_length=100),
        ),
    ]
