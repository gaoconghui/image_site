# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-17 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0003_auto_20170615_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
