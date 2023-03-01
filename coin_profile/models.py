from django.db import models


class CoinProfile(models.Model):
    coin_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200, primary_key=True, unique=True)
    rank = models.IntegerField()
    is_new = models.BooleanField()
    is_active = models.BooleanField()
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    message = models.CharField(max_length=200, null=True)
    open_source = models.BooleanField()
    started_at = models.DateField(auto_now=True)
    development_status = models.CharField(max_length=200, null=True)
    hardware_wallet = models.BooleanField()
    proof_type = models.CharField(max_length=200)
    org_structure = models.CharField(max_length=200, null=True)
    hash_algorithm = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        """
        A human-readable name for the object(s)
        that will be used in the Django admin interface. 
        """
        verbose_name_plural = "Coin Profile"
