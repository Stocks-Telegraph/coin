from django.db import models


# Create your models here.
class SocialLinks(models.Model):
    facebook= models.CharField(max_length=120)
    reddit= models.CharField(max_length=120)
    source_code= models.CharField(max_length=120)
    website= models.CharField(max_length=120)
    youtube_link= models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Social Links"
        
        
class ExplosureLinks(models.Model):
    explorer_link_1= models.CharField(max_length=120)
    explorer_link_2= models.CharField(max_length=120)
    explorer_link_3= models.CharField(max_length=120)
    explorer_link_4= models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Explosure Links"
        
