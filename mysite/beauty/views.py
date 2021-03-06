# coding=utf-8 #coding:utf-8
import logging
import random
from collections import Counter

from beauty.editor import editor_tags
from beauty.models import Gallery, Tag
from beauty.models import Image
from beauty.seo import seo_manager
from beauty.static_util import site_statistics, home_tags, tags_without_actor
from beauty.tags_model import tag_cache, Page
from beauty.tags_model import tag_info
from beauty.view_counter import view_counter
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from util.normal import ensure_utf8
from util.pinyin import get_pinyin
from hashlib import md5

logger = logging.getLogger("beauty")


@cache_page(60 * 15)
def index(request, page_num=1):
    if "tag_name" in request.GET:
        tag_name = request.GET.get("tag_name")
        if tag_name:
            page_num = request.GET.get("page", page_num)
            return tag_page(request, tag_name, page_num)
    page_num = int(page_num)
    context = {
        'page_content': __get_galleries_by_tag("all", 10, page_num, max_pages=100),
        'home_tags': home_tags()
    }
    return render(request, 'beauty/index.html', __with_index_seo(__with_normal_field(context)))


@cache_page(60 * 15)
def gallery(request, _id, page_num=1):
    context = gen_gallery(request, _id, page_num=page_num, page_size=1)
    return render(request, 'beauty/detail.html', __with_gallery_seo(__with_normal_field(context)))


@cache_page(60 * 15)
def gallery_more(request, _id, page_num):
    context = gen_gallery(request, _id, page_num=page_num, page_size=5)
    return render(request, 'beauty/detail_all.html', __with_gallery_seo(__with_normal_field(context)))


@cache_page(60 * 15)
def gallery_debug(request, _id, page_num):
    context = gen_gallery(request, _id, page_num=page_num, page_size=500)
    return render(request, 'beauty/detail_all.html', __with_gallery_seo(__with_normal_field(context)))


def tag_page(request, tag_name, page_num=1):
    """
    包含查询tag和query数据库两种，会优先查询tag
    :param request:
    :param tag_name:
    :param page_num:
    :return:
    """
    page_num = int(page_num)
    try:
        tag_id = get_pinyin(tag_name)
        tags = Tag.objects.filter(tag_id=tag_id)
        if len(tags) == 0:
            raise Tag.DoesNotExist
        tag = tags[0]
        galleries = __get_galleries_by_tag(tag_id, page_size=20, page=page_num, max_pages=100)
    except Tag.DoesNotExist:
        logger.info("tag not exist , need query {query}".format(query=ensure_utf8(tag_name)))
        # 每次都要扫表，很慢
        gs = Gallery.objects.filter(title__contains=tag_name)
        g_page = Paginator(gs, 20)
        g_list = g_page.page(page_num)
        galleries = Page(object_list=g_list.object_list, page_size=20, num_pages=g_page.num_pages, number=g_list.number)
        tag = {
            "tag_name": tag_name,
            "tag_id": tag_name
        }
    context = {
        'page_content': galleries,
        'tag': tag,
        'relate_tags': __get_relate_tags(galleries, tag_name)
    }
    tag_view = tag_info.info(get_pinyin(tag_name))
    if tag_view:
        context['tag_view'] = tag_view
    return render(request, 'beauty/tag_page.html', __with_tag_seo(__with_normal_field(context)))


@cache_page(24 * 3600)
def theme_page(request, page_num=1):
    """
    专题页面，展示tag
    :param request:
    :param page_num:
    :return:
    """
    result = []
    for item in editor_tags:
        tag_id, display_name = item
        tags = Tag.objects.filter(tag_id=tag_id)
        if len(tags) == 0:
            continue
        tag = tags[0]
        cover_id = tag_cache.query_by_tag(tag.tag_id, 1).get_objects()[0].cover_id
        result.append({
            "display_name": display_name,
            "tag_id": tag_id,
            "cover_id": cover_id
        })
    context = {
        "page_content": result
    }
    return render(request, 'beauty/theme_page.html', __with_index_seo(__with_normal_field(context)))


def __get_random_tag(count):
    """
    随机返回若干个tag(不包含actor)
    """
    tags = tags_without_actor()
    random.shuffle(tags)
    return tags[:count]


def gen_gallery(request, _id, page_num=1, page_size=1):
    view_counter.click(_id)
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
    if cache.get("gallery" + _id) is None:
        cache.set("gallery" + _id, get_random_galleries_by_tags(relate_tags, count=20), timeout=15 * 60)
    relate_galleries = cache.get("gallery" + _id)
    page = {
        "prev_gallery": _id,
        "next_gallery": _id if page_num < p.num_pages else random.choice(relate_galleries).gallery_id,
        "prev_page": page_num - 1 if page_num > 1 else 1,
        "next_page": page_num + 1 if page_num < p.num_pages else 1
    }
    context = {
        "gallery": _gallery,
        "image": image,
        "page": page,
        "relate_tags": relate_tags,
        "tags_cloud": relate_tags + __get_random_tag(20 - len(relate_tags)),
        "relate_galleries": relate_galleries,
        "tags_gallery": get_tag_gallery_map(relate_tags[:8], 10)
    }
    random.shuffle(context['tags_cloud'])
    return context


def __get_galleries_by_tag(tag, page_size, page, max_pages=-1):
    return tag_cache.query_by_tag(tag=tag, page_size=page_size, number=page, max_page=max_pages)


def get_random_galleries_by_tags(tags, count):
    # TODO 增加缓存  不一定是对这个方法加缓存，可以是对图集相关推荐的部分增加缓存
    pre_tag_count = [count / len(tags) for _ in tags]
    pre_tag_count[0] += count - sum(pre_tag_count)
    result = set()
    for index, tag in enumerate(tags):
        result.update(set(_get_random_galleries_by_tag(tag, pre_tag_count[index])))
    return list(result)


def get_tag_gallery_map(tags, max_count):
    """
    生成gallery页面右侧tag-gallery映射栏
    :param tags:
    :param max_count:
    :return:
    """
    result = []
    for tag in tags:
        item = {'tag': tag, 'galleries': set(_get_random_galleries_by_tag(tag, max_count))}
        result.append(item)
    return result


def _get_random_galleries_by_tag(tag, count):
    """
    获取与tag相关的最多count个图集
    :param tag:
    :param count:
    :return:
    """
    cache_id = md5(ensure_utf8(tag.get("tag_id") + str(count))).hexdigest()
    if cache.get(cache_id) is None:
        cache.set(cache_id, tag_cache.get_random_top10000_by_tag(tag.get("tag_id"), count), timeout=15 * 60)
    return cache.get(cache_id)


def __get_relate_tags(galleries, tag_id):
    """
    从图集中抽取tags
    按频率排序前20的tag （不能全部显示，全部显示会出现过多tag。
    :param galleries: 
    :return: 
    """
    if not galleries:
        return []
    if len(galleries) == 1:
        tag_names = galleries[0].tags.split(",")
        return [{"tag_name" : tag_name , "tag_id" : get_pinyin(tag_name)} for tag_name in tag_names]
    relate_tags = reduce(lambda x, y: x + y, [gallery.tags.split(",") for gallery in galleries])
    relate_tags = [{"tag_name": tag, "tag_id": get_pinyin(tag)} for tag in
                   [tag[0] for tag in Counter(relate_tags).most_common(35) if tag_id != get_pinyin(tag[0])]
                   ]
    return relate_tags


def __with_normal_field(context):
    """
    增加网站footer的展示数据
    :param context: 
    :return: 
    """
    context['site_statistics'] = site_statistics()
    return context


def __with_index_seo(context):
    seo = {
        "title": u"meizibar 妹子吧 - 清纯性感清新甜美萌妹子 高清大图欣赏",
        "keywords": u"meizi，妹子图，美女，美女图片，清纯，性感",
        "desc": u"meizibar 妹子吧，收集精美的妹子图片，上百种分类，包括性感可爱清纯，运动校花美女，车模浴室外围等好看的妹子图片。"
    }
    context['seo'] = seo
    return context


def __with_tag_seo(context):
    tag = context.get("tag")
    if isinstance(tag, Tag):
        tag_name = tag.tag_name
    else:
        tag_name = tag.get("tag_name")
    if not seo_manager.get_seo(tag_name):
        relate_tags = context.get("relate_tags")
        r_t_name = [t.get("tag_name") for t in relate_tags[0:3]]
        seo = {
            "title": u"{tag_name}_{relate_name}  - meizibar 妹子吧".format(tag_name=tag_name,
                                                                        relate_name="_".join(r_t_name)),
            "keywords": u"{tag_name}_{relate_name}".format(tag_name=tag_name, relate_name="_".join(r_t_name)),
            "desc": u"妹子吧{tag_name}频道为用户提供最优质的相关{tag_name}的高清图片。".format(tag_name=tag_name)
        }
        if tag_info.info(get_pinyin(tag_name)):
            seo['desc'] = (seo['desc'] + tag_info.info(get_pinyin(tag_name)).get("desc"))[:90]
        seo_manager.add_seo(tag_name, seo)
    context['seo'] = seo_manager.get_seo(tag_name)
    return context


def __with_gallery_seo(context):
    gallery = context.get("gallery")
    relate_tags = context.get("relate_tags")
    seo = {
        "title": gallery.title + " www.meizibar.com",
        "keywords": ",".join([t.get("tag_name") for t in relate_tags]),
        "desc": u"meizibar 妹子吧为您提供 {title}".format(title=gallery.title)
    }
    context['seo'] = seo
    return context


def handler404(request):
    return render(request, 'beauty/404.html', status=404)


def handler500(request):
    return render(request, 'beauty/500.html', status=500)
