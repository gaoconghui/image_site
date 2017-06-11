# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-11 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0002_auto_20170610_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='pages',
            new_name='all_page',
        ),
        migrations.AddField(
            model_name='gallery',
            name='domain',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='from_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='desc',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]