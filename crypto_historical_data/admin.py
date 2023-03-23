from django.contrib import admin
from .models import CryptoHistoricalData
# Register your models here.
class CryptoHistoricalDataAdmin(admin.ModelAdmin):
    list_per_page = 12
    search_fields = ['symbol__symbol']

admin.site.register(CryptoHistoricalData,CryptoHistoricalDataAdmin)