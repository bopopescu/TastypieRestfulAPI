from tastypie.resources import ModelResource
from results.models import *


class EntryResource(ModelResource):
    class Meta:
        queryset = accounts.objects.all()
        resource_name = 'entry'
