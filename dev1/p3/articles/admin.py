# -*- coding:utf-8 -*-

from django.contrib import admin

from articles.models import Article

# Pour plus de possibilités : Voir https://docs.djangoproject.com/en/1.6/intro/tutorial02/
admin.site.register(Article)