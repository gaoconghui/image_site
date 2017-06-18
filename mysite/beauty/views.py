# coding=utf-8 #coding:utf-8

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from beauty.models import Gallery, Tag
from beauty.models import Image
from beauty.static_util import site_statistics, home_tags
from beauty.tags_model import tag_cache
from util.pinyin import get_pinyin


def index(request, page_num=1):
    page_num = int(page_num)
    context = {
        'page_content': __get_galleries_by_tag("all", 10, page_num),
        'home_tags': home_tags()
    }
    return render(request, 'beauty/index.html', __with_normal_field(context))


def gallery(request, _id, page_num=1):
    page_num = int(page_num)
    _gallery = Gallery.objects.get(gallery_id=_id)
    all_images = Image.objects.filter(gallery_id=_id)

    p = Paginator(all_images, 1)
    if page_num > p.num_pages:
        page_num = p.num_pages
    if page_num <= 0:
        page_num = 1
    image = p.page(page_num)
    page = {
        "prev_gallery": _id,
        "next_gallery": _id,
        "prev_page": page_num - 1 if page_num > 1 else 1,
        "next_page": page_num + 1 if page_num < p.num_pages else p.num_pages
    }
    context = {
        "gallery": _gallery,
        "image": image,
        "page": page,
        "page_content": __get_galleries_by_tag("tag", page_size=20, page=1)
    }
    return render(request, 'beauty/detail.html', __with_normal_field(context))


def tag_page(request, tag_name, page_num=1):
    """
    TODO 需要改为从reids读取tag下的gallery
    :param request: 
    :param tag_name: 
    :param page_num: 
    :return: 
    """
    page_num = int(page_num)
    try:
        tag = Tag.objects.get(tag_id=tag_name)
    except Tag.DoesNotExist:
        raise Http404("Poll does not exist")
    galleries = __get_galleries_by_tag(tag_name, page_size=5, page=page_num)
    context = {
        'page_content': galleries,
        'tag': tag,
        'relate_tags': __get_relate_tags(galleries, tag_name)
    }
    return render(request, 'beauty/tag_page.html', __with_normal_field(context))


def __get_galleries_by_tag(tag, page_size, page):
    return tag_cache.query_by_tag(tag=tag, page_size=page_size, number=page)


def __get_relate_tags(galleries, tag_id):
    """
    从图集中抽取tags
    :param galleries: 
    :return: 
    """
    relate_tags = [gallery.tags.split(",") for gallery in galleries]
    relate_tags = [{"tag_name": tag, "tag_id": get_pinyin(tag)} for tag in set(reduce(lambda x, y: x + y, relate_tags))
                   if get_pinyin(tag) != tag_id]
    return relate_tags


def __with_normal_field(context):
    """
    增加网站footer的展示数据
    :param context: 
    :return: 
    """
    context['site_statistics'] = site_statistics()
    return context
