# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import HttpResponseRedirect
import random
from django.urls import reverse
from django.shortcuts import get_object_or_404
from shurl.settings import SITE_URL
from django.contrib import messages#

from shurlapp.models import *

# генерируем короткий url заданной длины
def generate_shurl(length):
	char = "ABCDEFGHIJKLMNOPQRTSUVWXYZabcdefghijklmnopqrtsuvwxyz0123456789"
	while True:
		shurl = "".join(random.choice(char) for x in range(length))
		# проверяем нет ли такого адреса в бд
		if not Url.objects.filter(shurl=shurl):
			return shurl

# Create your views here.
class shurl_create_or_find(CreateView):	
	template_name = "shurl_create_or_find.html"
	model = Url
	fields = ['url']

	def dispatch(self, request, *args, **kwargs):
		self.data = ''
		return super(shurl_create_or_find, self).dispatch(request, *args, **kwargs)
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		# делаем проверку нет ли данного url в БД
		# если есть, сразу возвращаем его
		res = Url.objects.filter(url=instance.url).first()
		if res:
			self.data = res.shurl
			return render(self.request, self.template_name, self.get_context_data(form=form))
		
		# # делаем проверку на случай если пользователь вставил короткую ссылку
		# res = Url.objects.filter(=instance.url).first()
		# if res:
		# 	self.data = res.shurl
		# 	return render(self.request, self.template_name, self.get_context_data(form=form))
		

		# генерируем короткий адрес
		self.data = generate_shurl(5)
		instance.shurl = self.data
		instance.save()
		messages.info(self.request, "Шурл успешно сгенерирован!")
		return render(self.request, self.template_name, self.get_context_data(form=form))

	def get_context_data(self, *args, **kwargs):
		context_data = super(shurl_create_or_find, self).get_context_data(*args, **kwargs)
		context_data.update({'shurl': self.data})
		return context_data

def redirect_to_shurl(request, slug):
	res = get_object_or_404(Url, shurl=slug)
	return HttpResponseRedirect(res.url)