import django
from django.db import models
from datetime import *

from django.contrib.auth.models import User
#
# class personal_info(models.Model):
#
# 	firstname = models.CharField(max_length=50, blank = True, null = True)
# 	lastname = models.DecimalField(max_length=30, decimal_places=3, max_digits=8, blank = True, null = True)
# 	address = models.CharField(max_length=300, blank = True, null = True)
# 	zipcode = models.CharField(max_length=300, blank = True, null = True)
# 	City =  models.CharField(max_length=300, blank = True, null = True)
# 	#radio button for beginner starting set
#

	# picture = models.CharField(max_length=3000, blank = True, null = True)
	# titlea = models.CharField(max_length=3000, blank = True, null = True)
	# message = models.TextField(blank = True, null = True)
	# picture =  models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
	# date_created = models.DateTimeField(default=datetime.now())
	# google_doc_link = models.CharField(max_length=3000, blank = True, null = True)



class accounts(models.Model):
	published = models.BooleanField(default = False)
	unaccounted_for_media_count = models.IntegerField(blank = True, null = True)
	media_count = models.IntegerField(blank = True, null = True)
	data_dump =  models.TextField(blank = True, null = True)
	user = models.CharField(max_length=3000, blank = True, null = True)
	hashtag = models.CharField(max_length=3000, blank = True, null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	link =  models.CharField(max_length=3000, blank = True, null = True)

class active_clients(models.Model):

	instagram_name = models.CharField(max_length = 300, blank = True, null = True)
	username = models.CharField(max_length = 300, blank = True, null = True)
	instagram_password = models.CharField(max_length = 300, blank = True, null = True)
	hashtags = models.CharField(max_length = 300, blank = True, null = True)
	active = models.BooleanField(default= False)



class media_liked(models.Model):
    client_name = models.TextField( blank = True, null = True)
    which_platform = models.CharField(max_length = 300, blank = True, null = True)
    client_instagram_id = models.TextField( blank = True, null = True)
    media_id_of_media = models.CharField(max_length = 300, blank = True, null = True)
    hashtag_of_media = models.CharField(max_length = 300, blank = True, null = True)
    url_to_media = models.TextField( blank = True, null = True)
    created_time = models.DateTimeField(default = django.utils.timezone.now)
    comment = models.CharField(max_length = 300, blank = True, null = True)
    commented = models.BooleanField(default= False)
    location_based = models.BooleanField(default= False)



class email_subscribers(models.Model):
    email = models.TextField( blank = True, null = True)
    beta_tester = models.BooleanField(default= False)





class instagram_codes(models.Model):
    instagram_code = models.TextField( blank = True, null = True)
    created_time = models.DateTimeField(default = django.utils.timezone.now)
    for_which_user = models.TextField( blank = True, null = True)
