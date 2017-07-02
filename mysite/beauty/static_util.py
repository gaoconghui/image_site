# coding=utf-8 #coding:utf-8
"""
记录网站一些比较静态的数据，后期会设置较长时间的缓存时间
"""
import time

from beauty.models import Tag, Gallery, Image


def home_tags():
    """
    index 页面展示的tags
    """
    return Tag.objects.all()[0:10]


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
