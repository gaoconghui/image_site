# Create your models here.
from django.db import models


class Gallery(models.Model):
    gallery_id = models.CharField(max_length=200)
    publish_time = models.IntegerField()
    insert_time = models.IntegerField()
    pages = models.IntegerField()
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Image(models.Model):
    gallery_id = models.CharField(max_length=200)
    image_id = models.CharField(max_length=200)
    order = models.IntegerField()

