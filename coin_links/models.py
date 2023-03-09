from django.db import models
from coin_profile.models import CoinProfile
# Create your models here
class SocialLinks(models.Model):
    symbol = models.ForeignKey(CoinProfile, to_field="symbol", on_delete=models.CASCADE)
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

        verbose_name_plural = "Social-links-of-coin"


class ExplorerLinks(models.Model):
    symbol = models.ForeignKey(CoinProfile, to_field="symbol", on_delete=models.CASCADE)
    explorer_link_1 = models.CharField(max_length=120, null=True)
    explorer_link_2 = models.CharField(max_length=120, null=True)
    explorer_link_3 = models.CharField(max_length=120, null=True)
    explorer_link_4 = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f"Explorer links: {self.explorer_link_1}"

    class Meta:
        verbose_name_plural = "Explorer-links-of-coin"
