from django.contrib import admin
from .models import ExplorerLinks, SocialLinks

# Register your models here.
class SocialLinksAdmin(admin.ModelAdmin):
    list_per_page = 12


class ExplorerLinksAdmin(admin.ModelAdmin):
    list_per_page = 12


admin.site.register(SocialLinks, SocialLinksAdmin)
admin.site.register(ExplorerLinks, ExplorerLinksAdmin)
