# -*- coding: utf-8 -*-
"""
seo相关操作
"""
import json
import os

from mysite.settings import BASE_DIR

beauty_dir = os.path.join(BASE_DIR, "beauty")

class SeoManager():
    """
    维护seo相关的内容
    """

    def __init__(self, seo_path):
        self.seo_path = seo_path
        with open(seo_path) as f:
            self.seo_data = json.load(f)

    def get_seo(self, key):
        return self.seo_data.get(key)

    def add_seo(self, key, item):
        self.seo_data[key] = item
        self.save()

    def save(self):
        with open(self.seo_path,'w') as f:
            s =json.dumps(self.seo_data, indent=2,ensure_ascii=False).encode("utf8")
            f.write(s)


seo_file = os.path.join(beauty_dir,"seo.json")
seo_manager = SeoManager(seo_file)
print seo_manager