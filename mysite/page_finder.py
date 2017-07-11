# -*- coding: utf-8 -*-
"""
给百度主动推链接收录
"""
# import os, django
import os

import jieba
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()
from beauty.models import Tag, Gallery
from beauty.tags_model import tag_cache
from util.pinyin import get_pinyin


def get_all_tag_page():
    base = "http://www.meizibar.com/{tag}/1"
    for t in Tag.objects.all():
        url = base.format(tag=t.tag_id)
        yield url

def get_all_gallery_page():
    base = "http://www.meizibar.com/gallery/{gallery}/more/1"
    for g in Gallery.objects.all():
        url = base.format(gallery=g.gallery_id)
        yield url

if __name__ == '__main__':
    url = "http://data.zz.baidu.com/urls?site=www.meizibar.com&token=gRFpxp8hn04BXTjV"
    # for u in get_all_gallery_page():
    #     print u
    #     r = requests.post(url,data=u)
    #     print r.text
    for u in get_all_tag_page():
        print u
        r = requests.post(url,data=u)
        print r.text