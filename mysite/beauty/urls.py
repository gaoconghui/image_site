from django.conf.urls import url
from django.conf import urls
from . import views

app_name = 'beauty'

urlpatterns = [
    # ex: /beauty/
    url(r'^$', views.index, name='index'),
    url(r'^recommend.*$', views.theme_page, name='theme'),
    url(r'^(?P<page_num>\d+)/$', views.index, name='hot'),
    url(r'^gallery/(?P<_id>\w+)/(?P<page_num>\d+)$', views.gallery, name='gallery'),
    url(r'^gallery/(?P<_id>\w+)/more/(?P<page_num>\d+)$', views.gallery_more, name='gallery_more'),
    url(r'^(?P<tag_name>.*?)/(?P<page_num>\d+)/$', views.tag_page, name='tag_page'),
]

urls.handler404 = views.handler404
urls.handler400 = views.handler404
urls.handler403 = views.handler404
urls.handler500 = views.handler404

