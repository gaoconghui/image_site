# -*- coding: utf-8 -*-
import json
import logging
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from beauty.models import Gallery, Image, Tag
from beauty.tags_model import tag_cache
from util.dedup import is_new_md5, add_title_to_md5
from util.normal import ensure_unicode, ensure_utf8
from util.pinyin import get_pinyin

push_key = u"mt1994"
logger = logging.getLogger("push")


def get_all_tags():
    all_tags = Tag.objects.all()
    all_tags = [tag.tag_id for tag in all_tags]
    return all_tags

@csrf_exempt
def gallery(request):
    result = {
        "status": "failed"
    }
    if request.method == 'POST':
        received_json_data = json.loads(ensure_unicode(request.body))
        key = received_json_data.get("key", "")
        if key != push_key:
            result['msg'] = "not authorize"
        else:
            # try:
            save_gallery_item(received_json_data)
            result['status'] = "success"
            # except IntegrityError:
            #     result['msg'] = "IntegrityError"
            print received_json_data
    else:
        result['msg'] = "need post"
    return HttpResponse(json.dumps(result), content_type='application/json')


def check(request, md5):
    return HttpResponse(is_new_md5(md5))


def save_gallery_item(data):
    """
    保存传进来的图集以及图片内容，格式如下
    {
        gallery : { gallery_field },
        images : [
            image
            image
            image
        ]
    }
    :param data: 
    :return: 
    """
    logger.debug(json.dumps(data))
    ori_gallery = data.get("gallery", {})
    title = ori_gallery['title']
    if not add_title_to_md5(ensure_utf8(title)):
        logger.info("dedup old title")
        return
    images = data.get("images", [])

    _gallery = Gallery.objects.create_item(
        gallery_id=ori_gallery['gallery_id'],
        title=ensure_unicode(ori_gallery['title']),
        tags=ensure_unicode(ori_gallery.get("tags", "")),
        cover_id=ori_gallery.get("cover_id"),
        publish_time=ori_gallery.get("publish_time", int(time.time())),
        insert_time=ori_gallery.get("insert_time", int(time.time())),
        page_count=ori_gallery.get("page_count", len(images))
    )
    _gallery.save()
    for _image in images:
        Image.objects.create_item(
            gallery_id=_image.get("gallery_id", _gallery.gallery_id),
            image_id=_image['image_id'],
            desc=ensure_unicode(_image.get("desc", "")),
            order=_image["order"]
        ).save()

    # 建立tag索引
    tags_pinyin = [get_pinyin(tag) for tag in ori_gallery.get("tags", "").split(",")]
    tags_pinyin.append("all")
    tag_cache.add_new_gallery(gallery_id=_gallery.gallery_id, tags=tags_pinyin)
    check_and_add_tags(ori_gallery.get("tags", "").split(","))


def check_and_add_tags(tags):
    for tag in tags:
        pinyin = get_pinyin(tag)
        if pinyin not in get_all_tags():
            Tag.objects.create_item(
                tag_name=tag,
                tag_id=pinyin,
                tag_type=1,
                desc=""
            ).save()
