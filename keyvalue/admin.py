from keyvalue.models import KeyValue
from django.contrib import admin

# Register your models here.
class KeyValueAdmin(admin.ModelAdmin):
    list_display = ['key','value','timestamp']

admin.site.register(KeyValue,KeyValueAdmin)