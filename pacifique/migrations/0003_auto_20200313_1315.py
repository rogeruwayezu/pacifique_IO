# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-13 11:15
from __future__ import unicode_literals

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('pacifique', '0002_auto_20200312_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=martor.models.MartorField(),
        ),
    ]
