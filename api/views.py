from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import *
# Create your views here.

class UrlViewSet(viewsets.ModelViewSet):
	queryset = Urls.objects.all()
	serializer_class = UrlSerializer

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
