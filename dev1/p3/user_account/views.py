# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from forms import MyRegistrationForm 
# replace: from django.contrib.auth.forms import UserCreationForm


def login(request):
    c={}
    c.update(csrf(request))
    return render (request, 'user_account/login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
    	auth.login(request, user)
        return HttpResponseRedirect('/user_account/loggedin')
        """
        if user.is_active:
            print("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
        """
    else:
        return HttpResponseRedirect('/user_account/invalid_login')

def loggedin(request):
	return render(request, 'user_account/loggedin.html',
		{'full_name': request.user.username})

def invalid_login(request):
	context = {}
	return render(request, 'user_account/invalid_login.html',context)

def logout(request):
    auth.logout(request)
    context = {}
    return render(request, 'user_account/logout.html', context)	

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        print "hello"
        if form.is_valid():
        	form.save() # YOU CAN ADD AN EMAIL CHECKIN HERE + ACCEPT CONDITIONS
        	return HttpResponseRedirect('/user_account/register_success')
    args={}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()

    print args
    return render(request, 'user_account/register.html', args)

def register_success(request):
	context ={}
	return render(request, 'user_account/register_success.html', context)













