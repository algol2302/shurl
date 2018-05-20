# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Urls(models.Model):
	id = models.AutoField(verbose_name='id', primary_key=True, unique=True)
	url = models.URLField(verbose_name='URL', max_length=255)
	shurl = models.SlugField(verbose_name='Короткий URL', max_length=5, unique=True)
	ctime= models.DateTimeField(verbose_name='Время создания', auto_now=True)

	def __str__(self):
		return '%s %s %s' % (self.id, self.url, self.shurl)