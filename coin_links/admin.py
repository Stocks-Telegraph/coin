from django.contrib import admin
from .models import ExplosureLinks, SocialLinks

# Register your models here.
class SocialLinksAdmin(admin.ModelAdmin):
    list_per_page = 12
    
class ExplosureLinksAdmin(admin.ModelAdmin):
    list_per_page = 12
    
    
admin.site.register(SocialLinks,SocialLinksAdmin)
admin.site.register(ExplosureLinks,ExplosureLinksAdmin)
