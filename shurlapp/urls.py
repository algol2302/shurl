# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.urls import path

from shurlapp.views import *

app_name = 'shurlapp'
urlpatterns = [
	#diagram
	url(r'^$', shurl_create_or_find.as_view(), name='shurl_create_or_find'),
	path('<slug>/', redirect_to_shurl, name='blog_detail'),

]





