from django.contrib import admin
from results.models import *
from models import *
# Register your models here.
admin.site.register(active_clients)
admin.site.register(email_subscribers)
# admin.site.register(accounts)
#
# #admin.site.register(initialquestion)
# from django.forms import TextInput, Textarea
# from django.db import models
#
#
#


class kevin(admin.ModelAdmin):
    list_display = ('hashtag', 'pk')

admin.site.register(accounts, kevin)
