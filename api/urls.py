# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from api.views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'url', UrlViewSet)

app_name = 'api'
urlpatterns = [
	# api
	url(r'^api/?', include(router.urls)),
	# url(r'^api-auth/?', include('rest_framework.urls', namespace='rest_framework')),
]





