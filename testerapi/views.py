 #!/usr/bin/python
from ast import *
from django.contrib.auth import authenticate,login, logout



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
            login(self.request, kevina)
            print self.request.user
            if kevina is None:
                data['error'] = True

            else:
                pass

        else:
            User.objects.create_user(self.kwargs['username'], 'lennon@thebeatles.com', self.kwargs['password'])
            kevina = authenticate(username=self.kwargs['username'], password=self.kwargs['password'])
            ApiKey.objects.create(key='1a23', user=kevina)
            data['apikey'] = '1a23'
        return data
