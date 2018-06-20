from django.contrib.auth.models import User
from rest_framework import serializers
from shurlapp.models import Url

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

class UrlSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Url
		fields = ('id', 'uuid', 'url', 'shurl', 'ctime')

class UrlSerializer2(serializers.ModelSerializer):
	class Meta:
		model = Url
		fields = ('id', 'uuid', 'url', 'shurl', 'ctime')
