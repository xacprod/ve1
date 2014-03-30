# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from user_account import views

urlpatterns = patterns('',

    # login/logout
    url(r'^login/$', 'user_account.views.login'),
    url(r'^auth/$', 'user_account.views.auth_view'),
    url(r'^logout/$', 'user_account.views.logout'),
    url(r'^loggedin/$', 'user_account.views.loggedin'),
    url(r'^invalid_login/$', 'user_account.views.invalid_login'),

    # first registration
    url(r'^register_user/$', 'user_account.views.register_user'),
    url(r'^register_success/$', 'user_account.views.register_success'),
)