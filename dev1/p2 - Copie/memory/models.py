# -*- coding:utf-8 -*-

from django.db import models

class MemoryItem (models.Model):
    """Questions a poser"""   
    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    priority = models.IntegerField(default = 6)
    pub_date = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
    	return self.question
