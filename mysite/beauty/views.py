# coding=utf-8 #coding:utf-8

from beauty.models import Gallery
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import register


def index(request, page_num=1):
    all_gallery = Gallery.objects.order_by('publish_time')
    p = Paginator(all_gallery, 50)
    context = {'hot_page': p.page(page_num)}
    return render(request, 'beauty/index.html', context)


def gallery(request):
    return HttpResponse("hello world")

def tag_page(request,tag_name,page_num=1):
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

