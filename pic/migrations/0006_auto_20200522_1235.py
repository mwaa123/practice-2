# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-22 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0005_auto_20200521_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
