# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from app0 import views

urlpatterns = patterns('',
    # ex: /app0/
    url(r'^$', views.index, name='index'),
    # ex: /app0/5/
    url(r'^polls/(?P<poll_id>\d+)/$', views.choice, name='choice'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

)