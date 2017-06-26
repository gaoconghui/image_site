# -*- coding: utf-8 -*-

import logging

from django.contrib import admin

from beauty.models import Gallery, Tag, Image
from beauty.tags_model import tag_cache
from util.normal import ensure_utf8

logger = logging.getLogger("admin")

admin.site.register(Gallery)
admin.site.register(Image)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag_name', 'tag_id',)

    def delete_model(self, request, obj):
        """
        TODO 清理相关tag的缓存
        删除tag，重量级操作
        1、找到所有包含这个tag的图集，修改tag字段
        2、删除redis中的tag索引
        3、删除该tag，刷新缓存
        :param request:
        :param obj:
        :return:
        """
        tag_name = obj.tag_name
        logger.info("delete tag {tag}".format(tag=ensure_utf8(tag_name)))
        gs = Gallery.objects.filter(tags__contains=tag_name)
        for gallery in gs:
            logger.info("delete tag for gallery : {g_id}".format(g_id=gallery.gallery_id))
            tag_list = gallery.tags.split(",")
            tag_list.remove(tag_name)
            gallery.tags = ",".join(tag_list)
            gallery.save()
        logger.info("delete from tag_cache {tag_id}".format(tag_id=obj.tag_id))
        tag_cache.delete_tag(obj.tag_id)
        logger.info("delete from db {tag_id}".format(tag_id=obj.tag_id))
        obj.delete()


admin.site.register(Tag, TagAdmin)
