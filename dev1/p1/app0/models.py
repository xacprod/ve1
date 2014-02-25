# -*- coding:utf-8 -*-

from django.db import models

class Poll(models.Model):
    """Questions a poser"""   
    question = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

    def __unicode__(self):
    	return self.question

class Choice(models.Model):
    """Choix de réponse au sondage"""
    proposition = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    poll = models.ForeignKey(Poll)

    def __unicode__(self):
    	return self.proposition
