from django.contrib import admin
from .models import TickerForSpecificCoin

# Register your models here.
class TickerForSpecificCoinAdmin(admin.ModelAdmin):
    list_per_page = 12
    
    
admin.site.register(TickerForSpecificCoin,TickerForSpecificCoinAdmin)
