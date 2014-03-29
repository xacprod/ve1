# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from articles.models import Article




def articles(request):
    language = 'en-gb' #in the cookie (client side)
    session_language = 'en-gb' #in the session (server side)

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']

    return render(request, 'articles/articles.html',
    	{'articles': Article.objects.all(),
    	 'language':language,
         'session_language': session_language })



def article (request, article_id=1):

    article = get_object_or_404(Article, pk=article_id)

    return render(request, 'articles/article.html',
    	{'article':article})



def language(request, language='en-gb'):

    response = HttpResponse("setting language to %s, both session and cookies are modified" % language)
	
    #Le cookie est defini sur un objet response avec set, on appelle une action
    response.set_cookie('lang', language)

    #La session est definie sur un objet request, on définie une session
    request.session['lang'] = language

    return response