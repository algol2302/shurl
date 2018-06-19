from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from api.serializers import UrlSerializer, UserSerializer, UrlSerializer2
from shurlapp.models import Url
# Create your views here.

class UrlViewSet(viewsets.ModelViewSet):
	queryset = Url.objects.all()
	serializer_class = UrlSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UrlListCreateAPIView(ListCreateAPIView):
	queryset = Url.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = UrlSerializer2
	lookup_field = 'uuid'

class UrlRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Url.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = UrlSerializer2
	lookup_field = 'uuid'
