#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import index, course, search, play, teacher, article, error

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^course/$', course, name='course'),
    url(r'^search/$', search, name='search'),
    url(r'^play/$', play, name='play'),
    url(r'^teacher/$', teacher, name='teacher'),
    url(r'^article/$', article, name='article'),
    url(r'^error/$', error, name='error'),
]
