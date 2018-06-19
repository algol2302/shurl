# -*- coding: utf-8 -*-
from django.db import models
import uuid as uuid_lib

# Create your models here.
class Url(models.Model):
	id = models.AutoField(verbose_name='id', primary_key=True, unique=True)
	url = models.URLField(verbose_name='URL', max_length=255)
	shurl = models.SlugField(verbose_name='Короткий URL', max_length=5, unique=True)
	ctime= models.DateTimeField(verbose_name='Время создания', auto_now=True)
	uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
	
	def __str__(self):
		return '%s %s %s %s' % (self.id, self.uuid, self.url, self.shurl)