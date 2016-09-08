 #!/usr/bin/python
from ast import *
from django.contrib.auth import authenticate,login, logout
import random
import string


from json import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import *
from django.shortcuts import render
from django.contrib.auth.models import *
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
import sys
from django import forms
from django.contrib.auth.models import User
from re import *

from math import *


from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse

from unicodedata import *
from django.utils.translation import ugettext_lazy as _
from results.models import *

from django.forms import *

from tastypie.models import ApiKey


class LogoutViewa(TemplateView):
    template_name = 'logout.html'

    def get_context_data(self, **kwargs):
        # print self.request.user
        logout(self.request)
        # pass
class SignupViewa(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):

        data = super(SignupViewa, self).get_context_data(**kwargs)
        data['error'] = False
        if User.objects.filter(username = self.kwargs['username']):

            kevina = authenticate(username=self.kwargs['username'], password=self.kwargs['password'])



            if kevina is None:
                data['error'] = True

            else:
                login(self.request, kevina)
                data['apikey'] = kevina.email
                self.request.session['USERNAME'] = kevina.username
                self.request.session['API_KEY'] = kevina.email

        else:
            api_keya = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
            # api_keya = "hello"
            User.objects.create_user(self.kwargs['username'], api_keya, self.kwargs['password'])
            kevina = authenticate(username=self.kwargs['username'], password=self.kwargs['password'])
            ApiKey.objects.create(key=api_keya, user=kevina)
            data['apikey'] = api_keya
            self.request.session['USERNAME'] = kevina.username
            self.request.session['API_KEY'] = kevina.email
        return data

def home(request):
    try:
        request.session['USERNAME']
    except Exception as e:
        request.session['USERNAME'] = 'USERNAME'

    try:
        request.session['API_KEY']
    except Exception as e:
        request.session['API_KEY'] = 'API_KEY'

    return render(request, "index.html", {'API_KEY':request.session['API_KEY'],'USERNAME':request.session['USERNAME']})
