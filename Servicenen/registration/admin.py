from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','city','district','area','address']
    list_display_links = ['user']
    list_editable = ['address']
    list_filter = ['user','city','district','area','address']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Village)
