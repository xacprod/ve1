# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from memory import views

urlpatterns = patterns('',
    # ex: memory/5/
    url(r'^$', views.display, name='display'),
    url(r'^(?P<mem_id>\d+)/suppr/$', views.suppr, name='suppr'),
    url(r'^(?P<mem_id>\d+)/change_priority/(?P<new_priority>\w+)/$', views.change_priority, name='change_priority'),
    url(r'^add/$', views.add, name='add'),
)