from tastypie.resources import ModelResource
from results.models import *

from tastypie.authorization import DjangoAuthorization
# from tastypie.authorization import BasicAuthorization
from django.contrib.auth.models import User
from tastypie import fields



class EntryResource(ModelResource):
    class Meta:
        queryset = accounts.objects.all()
        resource_name = 'entry'

        # authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']
        fields = ['username', 'created_at']



#
# POST (Create)
# curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"sdf":"sdlkfj","hashtag": "Another Post","user": "/api/v1/user/1/"}' http://localhost:8000/api/v1/entry/
#
# PUT (Edit)
# curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"body": "This will probably be my last post.", "pub_date": "2011-05-22T00:46:38", "slug": "another-post", "title": "Another Post", "user": "/api/v1/user/1/"}' http://localhost:8000/api/v1/entry/4/
#
# Collection of PUT
# curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"objects": [{"body": "Welcome to my blog!","id": "1","pub_date": "2011-05-20T00:46:38","resource_uri": "/api/v1/entry/1/","slug": "first-post","title": "First Post","user": "/api/v1/user/1/"},{"body": "I'm really excited to get started with this new blog. It's gonna be great!","id": "3","pub_date": "2011-05-20T00:47:30","resource_uri": "/api/v1/entry/3/","slug": "my-blog","title": "My Blog","user": "/api/v1/user/2/"}]}' http://localhost:8000/api/v1/entry/
#
# Deleting a Record
# curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/entry/4/
#
# Deleteing many Records
# curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/entry/
