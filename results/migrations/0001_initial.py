# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=False)),
                ('unaccounted_for_media_count', models.IntegerField(null=True, blank=True)),
                ('media_count', models.IntegerField(null=True, blank=True)),
                ('data_dump', models.TextField(null=True, blank=True)),
                ('user', models.CharField(max_length=3000, null=True, blank=True)),
                ('hashtag', models.CharField(max_length=3000, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(max_length=3000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='active_clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram_name', models.CharField(max_length=300, null=True, blank=True)),
                ('username', models.CharField(max_length=300, null=True, blank=True)),
                ('instagram_password', models.CharField(max_length=300, null=True, blank=True)),
                ('hashtags', models.CharField(max_length=300, null=True, blank=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='email_subscribers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.TextField(null=True, blank=True)),
                ('beta_tester', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='instagram_codes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram_code', models.TextField(null=True, blank=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('for_which_user', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='media_liked',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.TextField(null=True, blank=True)),
                ('which_platform', models.CharField(max_length=300, null=True, blank=True)),
                ('client_instagram_id', models.TextField(null=True, blank=True)),
                ('media_id_of_media', models.CharField(max_length=300, null=True, blank=True)),
                ('hashtag_of_media', models.CharField(max_length=300, null=True, blank=True)),
                ('url_to_media', models.TextField(null=True, blank=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.CharField(max_length=300, null=True, blank=True)),
                ('commented', models.BooleanField(default=False)),
                ('location_based', models.BooleanField(default=False)),
            ],
        ),
    ]
