# coding=utf-8 #coding:utf-8

from beauty.models import Gallery
from beauty.models import Image
from django.core.paginator import Paginator
from django.shortcuts import render


def index(request, page_num=1):
    page_num = int(page_num)
    all_gallery = Gallery.objects.order_by('publish_time')
    p = Paginator(all_gallery, 50)
    context = {'hot_page': p.page(page_num)}
    return render(request, 'beauty/index.html', context)


def gallery(request, _id, page_num):
    page_num = int(page_num)
    _gallery = Gallery.objects.get(id=_id)
    gallery_id = _gallery.gallery_id
    all_images = Image.objects.filter(gallery_id=gallery_id)

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
        "page" : page
    }
    return render(request, 'beauty/detail.html', context)


def tag_page(request, tag_name, page_num=1):
    """
    TODO 需要改为从reids读取tag下的gallery
    :param request: 
    :param tag_name: 
    :param page_num: 
    :return: 
    """
    all_gallery = Gallery.objects.order_by('publish_time')
    p = Paginator(all_gallery, 50)
    context = {'tag_page': p.page(page_num)}
    return render(request, 'beauty/tag_page.html', context)
