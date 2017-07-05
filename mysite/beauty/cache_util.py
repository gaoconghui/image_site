# -*- coding: utf-8 -*-

"""
缓存相关的方法
"""
import functools

from django.core.cache import cache



def fun_cache(timeout=30 * 60,key_getter=lambda x,y:1):
    """
    直接用装饰器的缓存，但是key获取出现了问题，不知道如何拿参数生成一个唯一性的key，先放弃了
    :param timeout:
    :param key_getter:
    :return:
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            key = func.__name__ + key_getter(args,kw)
            print key
            if key not in cache:
                print "cache"
                cache.set(key,func(*args,**kw),timeout)
            return cache.get(key)
        return wrapper
    return decorator



def static_cache(timeout=30 * 60):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            key = func.__name__
            if key not in cache:
                cache.set(key,func(*args,**kw),timeout)
            return cache.get(key)
        return wrapper
    return decorator