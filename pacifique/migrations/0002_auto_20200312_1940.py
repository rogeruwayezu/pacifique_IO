# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-12 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pacifique', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
