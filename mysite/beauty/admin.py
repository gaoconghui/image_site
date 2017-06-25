from django.contrib import admin

from beauty.models import Gallery, Tag, Image

admin.site.register(Gallery)
admin.site.register(Image)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag_name', 'tag_id',)

admin.site.register(Tag,TagAdmin)