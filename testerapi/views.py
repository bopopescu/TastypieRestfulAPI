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



from django.core.urlresolvers import reverse

from unicodedata import *
from django.utils.translation import ugettext_lazy as _
from results.models import *

from django.forms import *
