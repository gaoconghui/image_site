# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-15 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0002_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]