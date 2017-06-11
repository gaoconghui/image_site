# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-10 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_id', models.CharField(max_length=200)),
                ('publish_time', models.IntegerField()),
                ('insert_time', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_id', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
    ]
