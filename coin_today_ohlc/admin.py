from django.contrib import admin
from .models import Today_OHLC

# Register your models here.
class Today_OHLCAdmin(admin.ModelAdmin):
    list_per_page = 12
    search_fields = ['symbol__symbol'] 
    
admin.site.register(Today_OHLC,Today_OHLCAdmin)
