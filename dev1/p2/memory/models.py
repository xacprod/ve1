# -*- coding:utf-8 -*-

from django.db import models

class MemoryItem (models.Model):
    
    """Field.choices: option de Field pour définir un pré-choix"""

    #Les constantes et les valeurs courtes correspondantes à stocker"""
    MAITRISE = 'MAI'
    CONNU = 'CON'
    AREVOIR = 'AREV'
    IMPORTANT = 'IMP'
    PRIORITAIRE = 'PRIO'
    

    PRIORITY_CHOICE = (
   	# a droite, la valeur à afficher pour template (coté client) 
   	    (MAITRISE, u'Maitrisé'),
	    (CONNU, u'Connu'),
	    (AREVOIR, u'A revoir'),
	    (IMPORTANT, u'Important'),
	    (PRIORITAIRE, u'Prioritaire'),
	     )
    """Pour info, variante courte
	YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
	)"""


    """Questions a poser"""



    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    priority = models.CharField(max_length = 50, choices=PRIORITY_CHOICE,default=PRIORITAIRE)
    pub_date = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
    	return self.question



