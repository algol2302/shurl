# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from api.views import UserViewSet, UrlViewSet, UrlListCreateAPIView, UrlRetrieveUpdateDestroyAPIView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'url', UrlViewSet)

app_name = 'api'
urlpatterns = [
	# api
	url(r'^api/?', include(router.urls)),
	url(r'^api-auth/?', include('rest_framework.urls', namespace='rest_framework')),
	#
	url(r'^api2/$', UrlListCreateAPIView.as_view(), name='url_rest_api'),
	# /flavors/api/:slug/
	url(r'^api2/(?P<uuid>[-\w]+)/$',UrlRetrieveUpdateDestroyAPIView.as_view(), name='url_rest_api'),
]





