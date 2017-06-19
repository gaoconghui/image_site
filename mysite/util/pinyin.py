#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pypinyin import lazy_pinyin

from util.normal import ensure_unicode

cache = {}

def get_pinyin_list(s):
    s = ensure_unicode(s)
    return lazy_pinyin(s)


def get_pinyin(s):
    if s not in cache.keys():
        cache[s] = "".join(get_pinyin_list(s))
    return cache[s]


if __name__ == "__main__":
    str_input = 'all'
    print(get_pinyin(str_input))
