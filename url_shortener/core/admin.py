from django.contrib import admin
from .models import Url


class UrlAdmin(admin.ModelAdmin):
	list_display = ['original_url', 'short_url']
	search_fields = ['original_url', 'short_url']
	prepopulated_fields = {'slug':('short_url',)}

admin.site.register(Url,UrlAdmin)