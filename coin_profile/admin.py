from django.contrib import admin
from .models import CoinProfile

# Register your models here.
class CoinProfileAdmin(admin.ModelAdmin):
    search_fields = ['symbol', 'name']
    list_per_page = 12

admin.site.register(CoinProfile,CoinProfileAdmin)
