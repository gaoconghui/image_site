# coding=utf-8 #coding:utf-8
import datetime

from django import template

from beauty.models import Image
from beauty.view_counter import view_counter

register = template.Library()


@register.simple_tag(name="image")
def get_image_url(image):
    """
    根据imageid 返回url
    在内容没有传云端时，先采取随机返回image的方式
    :param image_id: 
    :return: 
    """
    base = "http://beauty07.b0.upaiyun.com/{image_id}"
    if isinstance(image, Image):
        url = base.format(image_id=image.image_id)
        if image.size > 300000:
            url += "!big"
        return url
    else:
        return base.format(image_id=image)


@register.simple_tag(name="thumb")
def get_thumb_url(image_id):
    """
    根据imageid 返回url
    在内容没有传云端时，先采取随机返回image的方式
    :param image_id: 
    :return: 
    """
    url = "http://beauty07.b0.upaiyun.com/{image_id}!home".format(image_id=image_id)
    return url


@register.simple_tag(name="time")
def time_format(t):
    return datetime.datetime.fromtimestamp(int(t)).strftime('%Y-%m-%d')


@register.simple_tag(name="view")
def view_getter(_id):
    return view_counter.get_view_count(_id)
