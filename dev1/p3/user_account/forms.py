# -*- coding:utf-8 -*-

#the file is directly in the project because the registration is considered like 
# aside the application that could be developped

from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
    	#we heritate from a model
    	model = User
    	#we chose the fields we need
    	fields = ('username', 'email', 'password1', 'password2')

    # we over write the save method of the forms.py in django file
    # search in site packages then django/contrib/auth/forms =>UserCreationForm
    def save(self, commit=True):

        user = super(UserCreationForm, self).save(commit=False)
        # we suspend the commit waiting for added datas

        # we save the password 
        user.set_password(self.cleaned_data["password1"])

        # we add the email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    # in parallel we change
    # the import in the view from UserCreationForm to MyRegistrationForm
    #