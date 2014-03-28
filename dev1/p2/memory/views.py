# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import random

from memory.models import MemoryItem


def display(request):
    
    priority_scale = MemoryItem.PRIORITY_CHOICE
    # Mixed list
    mem_list = list(MemoryItem.objects.all().order_by('?'))
    item = mem_list[0]

    return render(request, 'memory/display.html',{
        'item':item,
        'priority_scale':priority_scale,
        })

def change_priority(request, mem_id, new_priority):  

    item_with_new_priority = get_object_or_404(MemoryItem, pk=mem_id)
    item_with_new_priority.priority = new_priority.encode("utf-8")
    item_with_new_priority.save()
    return HttpResponseRedirect(reverse('memory:display'))

def suppr(request, mem_id):
    
    item_to_erase = get_object_or_404(MemoryItem, pk=mem_id)
    item_to_erase.delete()
    return HttpResponseRedirect(reverse('memory:display'))

def add(request):

    item = MemoryItem()
    if request.method=='POST':
        item.question = request.POST['question'].encode("utf-8")
        item.answer = request.POST['answer'].encode("utf-8")
        priority = request.POST['priority'].encode("utf-8")

        item.save()
        return HttpResponseRedirect(reverse('memory:display'))
    return HttpResponse('erreur')