# -*- coding: utf-8 -*-
import json
import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from beauty.models import Gallery, Image
from util.normal import ensure_unicode

push_key = u"mt1994"


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
            result['status'] = "success"
            save_gallery_item(received_json_data)
            print received_json_data
    else:
        result['msg'] = "need post"
    return HttpResponse(json.dumps(result), content_type='application/json')


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
    ori_gallery = data.get("gallery", {})
    images = data.get("images", [])

    _gallery = Gallery.objects.create_item(
        gallery_id=ori_gallery['gallery_id'],
        title=ori_gallery['title'],
        tags=ori_gallery.get("tags", ""),
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
            desc=_image.get("desc", ""),
            order=_image["order"]
        ).save()
