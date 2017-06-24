from django.conf.urls import url

from . import views

app_name = 'push'

urlpatterns = [
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^check/(?P<md5>.*)$', views.check, name='check'),
]