from django.conf.urls import url

from . import views

app_name = 'beauty'

urlpatterns = [
    # ex: /beauty/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page_num>\d+)/$', views.index, name='hot'),
    url(r'^gallery/(?P<_id>\w+)/(?P<page_num>\d+)$', views.gallery, name='gallery'),
    url(r'^(?P<tag_name>\w+)/(?P<page_num>\d+)/$', views.tag_page, name='tag_page'),
# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]