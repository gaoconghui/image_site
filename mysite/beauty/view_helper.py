from django.core.cache import cache
from beauty.models import Tag


def get_all_tags():
    if "all_tags" not in cache:
        cache.set("all_tags", list(Tag.objects.all()), timeout=15 * 60)
    return cache.get("all_tags")