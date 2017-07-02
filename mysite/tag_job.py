# -*- coding: utf-8 -*-
"""
tag重建脚本
根据分词结果给图集增加tag
"""
# import os, django
import os

import jieba

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()
from beauty.models import Tag, Gallery
from beauty.tags_model import tag_cache
from util.pinyin import get_pinyin


def rebuild_tags():
    all_tags = Tag.objects.all()
    all_tags = set([tag.tag_name for tag in all_tags])
    for index, gallery in enumerate(Gallery.objects.all()):
        print index
        gid = gallery.gallery_id
        print "process " + gid
        tags = set(gallery.tags.split(","))
        title = gallery.title
        print title
        cuts = set([tag for tag in list(jieba.cut(gallery.title, cut_all=True)) if tag in all_tags])
        news = cuts.difference(tags)
        if len(news) > 0:
            print "{gallery} need rebuild".format(gallery=gid)
            for n_tag in cuts:
                add_gallery_to_tag(gid, n_tag)
            tags.update(cuts)
            gallery.tags = ",".join(list(tags))
            gallery.save()
        else:
            print "gallery need not rebuild".format(gallery=gid)


def add_gallery_to_tag(gallery_id, tag):
    tag_pinyin = get_pinyin(tag)
    print "add tag " + tag_pinyin
    tag_cache.add_new_gallery(gallery_id=gallery_id, tags=[tag_pinyin])


def init_redis_tag():
    """
    应该只在第一次启动的时候使用，会扫gallery表，在redis里建立索引
    :return:
    """
    for index, gallery in enumerate(Gallery.objects.all()):
        print index
        gid = gallery.gallery_id
        print "process " + gid
        tags = set(gallery.tags.split(","))
        for n_tag in tags:
            add_tag_is_not_exist(n_tag)
            add_gallery_to_tag(gid, n_tag)
        add_gallery_to_tag(gid, "all")


def add_tag_is_not_exist(tag_name):
    ts = Tag.objects.filter(tag_name=tag_name)
    if len(ts) == 0:
        print "add tag"
        tag_id = get_pinyin(tag_name)
        Tag.objects.create_item(
            tag_name=tag_name,
            tag_id=tag_id,
            tag_type=1,
            desc=""
        ).save()


def fix_tag_name():
    """
    老的tag中包含有空格的，用_代替
    :return: 
    """
    for index, gallery in enumerate(Gallery.objects.all()):
        print index
        tags = gallery.tags
        if " " in tags:
            print "tags is {tags}".format(tags=tags)
            tags = tags.replace(" ", "_")
            gallery.tags = tags
            gallery.save()


def update_tag_meta():
    f = open("./tag_meta")
    datas = f.readlines()
    datas = [data.replace("\n", '').split("\t") for data in datas]
    for data in datas:
        tag_name = data[1]
        tag_type = data[-1]
        ts = Tag.objects.filter(tag_name=tag_name)
        if len(ts) == 0:
            print "tag does not exist {tag}".format(tag=tag_name)
        else:
            for t in ts:
                t.tag_type = int(tag_type)
                t.save()


if __name__ == '__main__':
    # jieba.load_userdict("./userdict")
    # init_redis_tag()
    update_tag_meta()