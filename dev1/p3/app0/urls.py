# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from app0 import views

urlpatterns = patterns('',
    # ex: /app0/
    url(r'^$', views.index, name='index'),
    # ex: /app0/5/
    # url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
)