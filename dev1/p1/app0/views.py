# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from app0.models import Poll, Choice

def index(request): # display a list of polls
	
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request, 'app0/polls.html', {'latest_poll_list' : latest_poll_list})

def choice(request, poll_id):
    
    poll = get_object_or_404 (Poll,pk=poll_id)
    return render (request, 'app0/choices.html',{'poll':poll} )

def results(request, poll_id):
    
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'app0/results.html', {'poll':poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    	# Redisplay the poll voting form
    	return render(request, 'app0:choice', {
    	    'poll':p,
    	    'error_message':'You did not select a choice.',
    		})
    else:
    	selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app0:results',args=(p.id,)))

