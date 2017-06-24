from django.contrib import admin

# Register your models here.
from beauty.models import Gallery, Tag, Image

admin.site.register(Gallery)
admin.site.register(Tag)
admin.site.register(Image)