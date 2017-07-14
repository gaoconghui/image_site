# -*- coding: utf-8 -*-
"""
给百度主动推链接收录
"""

# import os, django
import os

import itertools

from mysite.settings import STATIC_ROOT
from util.normal import ensure_utf8

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()
from beauty.models import Tag, Gallery

def get_all_tag_page():
    base = "http://www.meizibar.com/{tag}/1"
    for t in Tag.objects.all():
        url = base.format(tag=ensure_utf8(t.tag_id))
        yield url


def get_all_gallery_page():
    base = "http://www.meizibar.com/gallery/{gallery}/1"
    for g in Gallery.objects.all():
        url = base.format(gallery=g.gallery_id)
        yield url

def get_all_gallery_more_page():
    base = "http://www.meizibar.com/gallery/{gallery}/more/1"
    for g in Gallery.objects.all():
        url = base.format(gallery=g.gallery_id)
        yield url


def gen_site_map(domain="normal"):
    """
    每五万个链接为一个文件，生成sitemap
    :return: 
    """
    if domain is "baidu":

        base = """<?xml version="1.0" encoding="UTF-8"?>
            <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
                    xmlns:mobile="http://www.baidu.com/schemas/sitemap-mobile/1/">
            {items}
            </urlset>
        """
    else:
        base = """<?xml version="1.0" encoding="UTF-8"?>
            <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            {items}
            </urlset>
        """

    def gen_url_item(url, priority, changefreq):
        if domain is "baidu":
            return "<url><loc>{url}</loc><priority>{priority}</priority><mobile:mobiletype=\"htmladapt\"/><changefreq>{changefreq}</changefreq></url>".format(
                url=url, priority=priority, changefreq=changefreq
            )
        return "<url><loc>{url}</loc><priority>{priority}</priority><changefreq>{changefreq}</changefreq></url>".format(
            url=url, priority=priority, changefreq=changefreq
        )

    index_items = [gen_url_item("http://www.meizibar.com",1.0,"always")]
    tag_items = [gen_url_item(url,0.8,"daily") for url in get_all_tag_page()]
    gallery_items = [gen_url_item(url,0.6,'weekly') for url in get_all_gallery_page()]
    gallery_items_more = [gen_url_item(url,0.6,'weekly') for url in get_all_gallery_more_page()]
    xml = base.format(items="\n".join(itertools.chain(index_items,tag_items,gallery_items,gallery_items_more)))
    with open(os.path.join(STATIC_ROOT,"{domain}_site_map.xml").format(domain=domain),"w") as f:
        print STATIC_ROOT
        f.write(xml)


if __name__ == '__main__':
    # url = "http://data.zz.baidu.com/urls?site=www.meizibar.com&token=gRFpxp8hn04BXTjV"
    # for u in get_all_gallery_page():
    #     print u
    #     r = requests.post(url,data=u)
    #     print r.text
    # for u in get_all_tag_page():
    #     print u
    #     r = requests.post(url, data=u)
    #     print r.text
    print gen_site_map("beauty")
    print gen_site_map("baidu")