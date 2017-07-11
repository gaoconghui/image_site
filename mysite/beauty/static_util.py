# coding=utf-8 #coding:utf-8
"""
记录网站一些比较静态的数据，后期会设置较长时间的缓存时间
"""
import random
import time

from beauty.cache_util import static_cache
from beauty.models import Tag, Gallery, Image


@static_cache(timeout=15 * 60)
def home_tags():
    """
    index 页面展示的tags
    """
    tags = tags_without_actor()
    random.shuffle(tags)
    return tags[0:10]


@static_cache(timeout=15 * 60)
def site_statistics():
    """
    网站的统计数据
    """
    result = {
        "num_gallery": __format_count(Gallery.objects.count()),
        "num_tag": Tag.objects.count(),
        "num_image": __format_count(Image.objects.count()),
        "running_time": (int(time.time()) - 1497768940) / 86400,
        "last_week_publish": Gallery.objects.filter(insert_time__gt=int(time.time() - 86400 * 7)).count()
    }
    return result


@static_cache(timeout=15 * 60,local=True)
def all_tags():
    return list(Tag.objects.all())


@static_cache(timeout=15 * 60,local=True)
def tags_without_actor():
    """
    所有不包含演员的tag
    :return:
    """
    return list(Tag.objects.filter(tag_type__in=[4, 3]))


def __format_count(num):
    """
    对数字进行格式化
    :param num:
    :return:
    """
    num *= 2
    if num < 10000:
        return num
    if 10000 < num < 100000:
        return str(num / 1000) + "千"
    if 100000 < num < 1000000:
        return str(num / 10000) + "万"
    return str(num / 1000000 + 1) + "百万"
