from django.contrib import admin
from .models import TickerForSpecificCoin

# Register your models here.
class TickerForSpecificCoinAdmin(admin.ModelAdmin):
    list_per_page = 12
    search_fields = ['symbol__symbol'] 
    
    
admin.site.register(TickerForSpecificCoin,TickerForSpecificCoinAdmin)
