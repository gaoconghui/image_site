# -*- coding: utf-8 -*-

from django.db import models

from util.normal import ensure_utf8

"""
model与爬取的model不同，这里完全不包含原始图片的信息，只包含线上展示的内容
"""


class ItemManager(models.Manager):
    def create_item(self, **kwargs):
        item = self.create(**kwargs)
        return item


class Gallery(models.Model):
    gallery_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, null=True)
    cover_id = models.CharField(max_length=200)
    publish_time = models.IntegerField(default=0)
    insert_time = models.IntegerField(default=0)
    page_count = models.IntegerField()

    objects = ItemManager()

    def __str__(self):
        return ensure_utf8(self.title)


class Image(models.Model):
    gallery_id = models.CharField(max_length=200)
    image_id = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=4096, null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    order = models.IntegerField()

    objects = ItemManager()

    def __str__(self):
        return self.image_id


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    tag_id = models.CharField(max_length=200)
    desc = models.CharField(max_length=1024, default="")
    tag_type = models.IntegerField()
    objects = ItemManager()

    def __str__(self):
        return "{name} -- {_id}".format(name=ensure_utf8(self.tag_name), _id=ensure_utf8(self.tag_id))
