# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from drag_drop import views

urlpatterns = patterns('',
    # ex: /drag_drop/
    #url(r'^$', views.index, name='index'),
    # ex: /drag_drop/5/
    # url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
)