# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0009_translator_success_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='submitted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
