from django.contrib import admin
from .models import PerformanceChange

# Register your models here.
class PerformanceChangeAdmin(admin.ModelAdmin):
    list_per_page = 12


admin.site.register(PerformanceChange, PerformanceChangeAdmin)
