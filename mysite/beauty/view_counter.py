# -*- coding: utf-8 -*-

"""
统计图集的点击数量，基于redis
"""
import redis


class ViewCounter():
    def __init__(self):
        self.r = redis.Redis()
        self.view_key = "view"

    def click(self, gallery_id):
        return self.r.hincrby(self.view_key, gallery_id, 1)

    def get_view_count(self, gallery_id):
        count = self.r.hget(self.view_key, gallery_id)
        return count if count else 0

    def get_view_map(self, gallery_ids):
        return {x: self.get_view_count(x) for x in gallery_ids}


view_counter = ViewCounter()
