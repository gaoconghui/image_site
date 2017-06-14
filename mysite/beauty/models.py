# Create your models here.
from django.db import models


class Gallery(models.Model):
    gallery_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, null=True)
    from_id = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    publish_time = models.IntegerField(null=True)
    insert_time = models.IntegerField(null=True)
    all_page = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    gallery_id = models.CharField(max_length=200)
    image_id = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    order = models.IntegerField()


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    tag_id = models.CharField(max_length=200)
