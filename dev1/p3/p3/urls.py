# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p3.views.home', name='home'),
    url(r'^articles/', include('articles.urls', namespace="articles")),

    url(r'^admin/', include(admin.site.urls)),
)