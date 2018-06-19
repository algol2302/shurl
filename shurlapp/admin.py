from django.contrib import admin

# Register your models here.
from .models import *

class shurlappAdmin(admin.ModelAdmin):
	list_display = ('id', 'shurl',)
admin.site.register(Url, shurlappAdmin)