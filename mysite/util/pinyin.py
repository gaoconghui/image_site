#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pypinyin import lazy_pinyin

from util.normal import ensure_unicode


def get_pinyin_list(s):
    s = ensure_unicode(s)
    return lazy_pinyin(s)


def get_pinyin(s):
    return "".join(get_pinyin_list(s))


if __name__ == "__main__":
    str_input = '我是中国人'
    print get_pinyin(str_input)
