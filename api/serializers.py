# from django.contrib.auth.models import User
from rest_framework import serializers
from shurlapp.models import *

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('url', 'username', 'email', 'is_staff')
class UrlSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Urls
		fields = ('id', 'url', 'shurl', 'ctime')
