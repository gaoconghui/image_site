# -*- coding: utf-8 -*-
import logging

import redis as redis
from django.conf import settings

"""
反爬虫中间件
反爬虫思路如下：
    1、只针对gallery页面反爬虫
    2、在tag_page 或Index中 或其他任意进入gallery的入口增加fake的gallery，前端通过js删除，如果点进去了就是爬虫
    3、fake的思路为通过某一算法计算fakeid，如果都是固定的id会出现去重后跳过的可能
    3、只记录做其他处理
"""

logger = logging.getLogger("beauty")


class AntiSpiderMiddleware(object):
    def __init__(self):
        super(AntiSpiderMiddleware, self).__init__()
        self.fake_id = settings.FAKE_ID
        self.r = redis.Redis()

    def process_request(self, request):
        path = request.path.lstrip("/")
        print path
        if self.fake_id in path:
            if request.META.has_key('HTTP_X_FORWARDED_FOR'):
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
            logger.warning("anti spider : {ip}".format(ip=ip))
            self.r.lpush("anti_spider",ip)
