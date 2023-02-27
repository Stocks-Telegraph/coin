from django.db import models

# Create your models here
class SocialLinks(models.Model):
    facebook = models.CharField(max_length=120, null=True)
    reddit = models.CharField(max_length=120, null=True)
    source_code = models.CharField(max_length=120, null=True)
    website = models.CharField(max_length=120, null=True)
    youtube_link = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f"Social links for {self.website}"

    class Meta:
        """
        A human-readable name for the object(s)
        that will be used in the Django admin interface. 
        """
        verbose_name_plural = "Social Links"


class ExplosureLinks(models.Model):
    explorer_link_1 = models.CharField(max_length=120, null=True)
    explorer_link_2 = models.CharField(max_length=120, null=True)
    explorer_link_3 = models.CharField(max_length=120, null=True)
    explorer_link_4 = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f"Exploration links: {self.explorer_link_1}"

    class Meta:
        verbose_name_plural = "Explosure Links"
