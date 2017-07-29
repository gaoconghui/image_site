# -*- coding: utf-8 -*-

"""
使用redis 来存储tag索引，每个tag都是一个zset，里边存着图集的score和图集id
每个图集会有多个tag
图集score会有加分减分操作
会有从tag中，随机抽取操作（最好是按score概率分布）
"""
import collections
import json
import os
import random
import time

import redis
import six
from beauty.models import Gallery
from mysite.settings import BASE_DIR
from util.pinyin import get_pinyin


class TagCache():
    def __init__(self):
        self.r = redis.Redis("localhost", db=1)

    def add_new_gallery(self, gallery_id, tags, priority=None):
        """
        为一个图集建立索引，如果已经建立过索引则直接跳过，所以这个方法可以随便用，不会造成线上数据被重置
        :param priority:
        :param gallery_id:
        :param tags: list of tag_id
        :return: 
        """
        if not priority:
            priority = int(-time.time())
        for tag in tags:
            if not self.r.zrank(tag, gallery_id):
                self.r.zadd(tag, gallery_id, int(priority))

    def remove_gallery(self, gallery_id, tags):
        """
        删除tags中的gallery
        :param gallery_id:
        :param tags:
        :return:
        """
        for tag in tags:
            self.r.zrem(tag, gallery_id)

    def delete_tag(self, tag_id):
        self.r.delete(tag_id)

    def query_by_tag(self, tag, page_size, number=1, max_page=-1):
        """
        核心方法，根据score排序获取图集
        :param max_page: 最多显示多少页
        :param tag: 要查询的tag，为拼音
        :param page_size: 每页数量
        :param number: 页数，默认第一页，如果小于1则默认1，大于最大值则最后一页
        :return: list of galleries
        """
        count = self.r.zcard(tag)
        num_pages = int((count - 1) / page_size) + 1
        if 0 < max_page < num_pages:
            num_pages = max_page
        if number < 1:
            number = 1
        if number > num_pages:
            number = num_pages
        galleries = self.r.zrange(tag, start=(number - 1) * page_size, end=number * page_size - 1)
        # TODO 必须要加cacha，不然要炸
        galleries = [Gallery.objects.get(gallery_id=gid) for gid in galleries]
        return Page(page_size, number, num_pages, galleries)

    def get_random_top10000_by_tag(self, tag, count):
        """
        从排名前一万种随机选出图集
        :param tag: 标签拼音
        :param count: 数量
        :return: 
        """
        all_count = self.r.zcard(tag)
        start = 0
        end = 10000 if all_count > 10000 else all_count - 1
        random_list = [random.randint(start, end) for _ in range(count)]
        random_galleries = [self.r.zrange(tag, index, index)[0] for index in random_list]
        random_galleries = [Gallery.objects.get(gallery_id=gid) for gid in random_galleries]
        return random_galleries

    def count(self,tag_id):
        return self.r.zcard(tag_id)

class Page(collections.Sequence):
    """
    包含页面的一些属性
    """

    def __init__(self, page_size, number, num_pages, object_list):
        self.page_size = page_size
        self.number = number
        self.object_list = object_list
        self.num_pages = num_pages

    def __repr__(self):
        return '<Page %s of %s>' % (self.number, self.num_pages)

    def __len__(self):
        return len(self.object_list)

    def __getitem__(self, index):
        if not isinstance(index, (slice,) + six.integer_types):
            raise TypeError
        # The object_list is converted to a list so that if it was a QuerySet
        # it won't be a database hit per __getitem__.
        if not isinstance(self.object_list, list):
            self.object_list = list(self.object_list)
        return self.object_list[index]

    def has_next(self):
        return self.number < self.num_pages

    def has_previous(self):
        return self.number > 1

    def has_other_pages(self):
        return self.has_previous() or self.has_next()

    def next_page_number(self):
        return self.number + 1 if self.number < self.num_pages else self.num_pages

    def previous_page_number(self):
        return self.number - 1 if self.number > 1 else 1

    def get_objects(self):
        return self.object_list


tag_cache = TagCache()


class TagViewManager(object):
    """
    tag 展示时候的背景 话术 先用文件的形式，以后考虑改为json形式存在tag表里头
    """

    def __init__(self, file_path):
        self.actors_map = {}
        with open(file_path, "r") as f:
            for actor in json.load(f):
                if "bg_key" in actor:
                    for name in actor.get("meta").split(","):
                        self.actors_map[get_pinyin(name)] = actor

    def info(self, tag_name):
        """
        最长的name + desc要小于158字符
        :param tag_name:
        :return:
        """
        if tag_name in self.actors_map:
            actor = self.actors_map.get(tag_name)
            len_max_desc = 158 - len(actor.get("name"))
            actor["desc"] = actor.get("desc")[:len_max_desc]
            return self.actors_map.get(tag_name)
        return None


os.path.dirname(BASE_DIR)
beauty_dir = os.path.join(os.path.dirname(BASE_DIR), "script")
info_file = os.path.join(beauty_dir, "actor.json")
tag_info = TagViewManager(info_file)
