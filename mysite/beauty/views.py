# coding=utf-8 #coding:utf-8

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from beauty.models import Gallery, Tag
from beauty.models import Image
from beauty.static_util import site_statistics, home_tags
from beauty.tags_model import tag_cache
from util.pinyin import get_pinyin

relate_gallery_cache = {}


def index(request, page_num=1):
    page_num = int(page_num)
    context = {
        'page_content': __get_galleries_by_tag("all", 10, page_num),
        'home_tags': home_tags()
    }
    return render(request, 'beauty/index.html', __with_normal_field(context))


def gallery(request, _id, page_num=1):
    context = gen_gallery(request, _id, page_num=page_num, page_size=1)
    return render(request, 'beauty/detail.html', __with_normal_field(context))


def gallery_more(request, _id, page_num):
    context = gen_gallery(request, _id, page_num=page_num, page_size=5)
    return render(request, 'beauty/detail_all.html', __with_normal_field(context))


def gen_gallery(request, _id, page_num=1, page_size=1):
    page_num = int(page_num)
    try:
        _gallery = Gallery.objects.get(gallery_id=_id)
    except Gallery.DoesNotExist:
        raise Http404("Gallery does not exist")
    all_images = Image.objects.filter(gallery_id=_id)

    p = Paginator(all_images, page_size)
    if page_num > p.num_pages:
        page_num = p.num_pages
    if page_num <= 0:
        page_num = 1
    image = p.page(page_num)
    relate_tags = __get_relate_tags([_gallery], "")
    page = {
        "prev_gallery": _id,
        "next_gallery": _id,
        "prev_page": page_num - 1 if page_num > 1 else 1,
        "next_page": page_num + 1 if page_num < p.num_pages else p.num_pages
    }
    if _id not in relate_gallery_cache:
        relate_gallery_cache[_id] = get_random_galleries_by_tags(relate_tags, count=10)
    relate_galleries = relate_gallery_cache[_id]
    context = {
        "gallery": _gallery,
        "image": image,
        "page": page,
        "page_content": __get_galleries_by_tag("tag", page_size=20, page=1),
        "relate_tags": relate_tags,
        "relate_galleries": relate_galleries
    }
    return context


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


def get_random_galleries_by_tags(tags, count):
    # TODO 增加缓存  不一定是对这个方法加缓存，可以是对图集相关推荐的部分增加缓存
    pre_tag_count = [count / len(tags) for _ in tags]
    pre_tag_count[0] += count - sum(pre_tag_count)
    result = set()
    for index, tag in enumerate(tags):
        result.update(set(tag_cache.get_random_top10000_by_tag(tag.get("tag_id"), pre_tag_count[index])))
    return list(result)


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
