import django
from django.db import models
from datetime import *

from django.contrib.auth.models import User


class accounts(models.Model):
	info = models.CharField(max_length=3000, blank = True, null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# user = models.CharField(max_length=3000, blank = True, null = True)
	user = models.ForeignKey(User, null=True)


# accounts.objects.create(info='Paid for the servers',user=u)
# http://localhost:8000/api/v1/entry/?format=json&username=kevin&api_key=1a23
# accounts.objects.create(infoa='Paid for the servers',user=u)
# headers = {'Content-type': 'application/json'}
# post_data = {'info': 'Bought Two scoops of Django'}
# r = requests.post("http://localhost:8000/api/v1/entry/?username=kevin&api_key=1a23", data=json.dumps(post_data), headers=headers)
# r = requests.post("http://localhost:8000/api/expense/?username=sheryl&api_key=1a23", data=json.dumps(post_data), headers=headers)

# http://localhost:8000/api/v1/entry/?format=json&username=kevin&api_key=1a23
