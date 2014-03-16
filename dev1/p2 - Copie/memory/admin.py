# -*- coding:utf-8 -*-

from django.contrib import admin

# REGISTER  YOUR MODELS HERE TO BE ABLE TO CONFIGURE THEM 
from memory.models import MemoryItem

# Pour plus de possibilités : Voir https://docs.djangoproject.com/en/1.6/intro/tutorial02/
admin.site.register(MemoryItem)
