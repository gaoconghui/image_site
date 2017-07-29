# -*- coding: utf-8 -*-

import logging

from beauty.models import Gallery, Tag, Image
from beauty.tags_model import tag_cache
from django.contrib import admin
from util.normal import ensure_utf8
from util.pinyin import get_pinyin

logger = logging.getLogger("beauty")

admin.site.register(Image)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag_name', 'tag_id',)
    fields = ('tag_name', 'desc', 'tag_type')

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
        # 存在tag包含的情况
        gs = Gallery.objects.filter(tags__contains=tag_name + ",") | Gallery.objects.filter(
            tags__contains="," + tag_name)
        for gallery in gs:
            logger.info("delete tag for gallery : {g_id}".format(g_id=gallery.gallery_id))
            tag_list = gallery.tags.split(",")
            tag_list.remove(tag_name)
            gallery.tags = ",".join(tag_list)
            gallery.save()
        logger.info("delete from tag_cache {tag_id}".format(tag_id=ensure_utf8(obj.tag_id)))
        tag_cache.delete_tag(obj.tag_id)
        logger.info("delete from db {tag_id}".format(tag_id=ensure_utf8(obj.tag_id)))
        obj.delete()

    def save_model(self, request, obj, form, change):
        """
        新增或更新tag，重量级操作
        1、数据库中查找tag_name不存在，存在则直接返回
        2、数据库中插入tag
        3、按照gallery 标题进行查找，标题中存在的则加入该tag
        4、新建索引
        """
        if change:
            obj.save()
        tags = Tag.objects.filter(tag_name=obj.tag_name)
        if len(tags) == 0:
            obj.tag_id = get_pinyin(obj.tag_name)
            obj.save()

            gs = Gallery.objects.filter(title__contains=ensure_utf8(obj.tag_name))
            for gallery in gs:
                logger.info("add tag for gallery : {gid}".format(gid=gallery.gallery_id))
                print
                tag_cache.add_new_gallery(gallery.gallery_id, [obj.tag_id])
                tag_list = gallery.tags.split(",")
                tag_list.append(obj.tag_name)
                gallery.tags = ",".join(tag_list)
                gallery.save()
        else:
            obj = tags[0]


class GalleryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'gallery_id',)

    def delete_model(self, request, obj):
        """
        删除Gallery，重量级操作
        1、删除redis中的索引
        2、删除图片
        3、删除图集
        :param request:
        :param obj:
        :return:
        """
        gallery_id = obj.gallery_id
        logger.info("delete gallery {gallery_id}".format(gallery_id=obj.gallery_id))
        tags = [get_pinyin(tag) for tag in obj.tags.split(",")]
        tags.append("all")
        tag_cache.remove_gallery(gallery_id, tags)
        for image in Image.objects.filter(gallery_id=gallery_id):
            image.delete()
        obj.delete()


admin.site.register(Tag, TagAdmin)
admin.site.register(Gallery, GalleryAdmin)
