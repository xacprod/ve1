# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',

    url(r'^all/$', views.articles, name='articles'),
    url(r'^get/(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^language/(?P<language>[a-zA-Z\-]+)/$', views.language, name='language'),
    #url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
)