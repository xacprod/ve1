# -*- coding:utf-8 -*-

from django.db import models
from time import time



class Article (models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title




"""
def get_upload_file_name(instance,filename):
	return "uploaded_files/%s_%s"(str(time()).replace('.','_').filename)


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    thumbnail = models.FileField(upload_to=get_upload_file_name)
    def __unicode__(self):  # Python 3: def __str__(self):
	        return self.question

"""