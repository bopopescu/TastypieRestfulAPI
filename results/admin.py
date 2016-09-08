from django.contrib import admin
from results.models import *
from models import *
# Register your models here.

class kevin(admin.ModelAdmin):
    list_display = ('info', 'user')

admin.site.register(accounts, kevin)
#
# #admin.site.register(initialquestion)
# from django.forms import TextInput, Textarea
# from django.db import models
#
#
#
