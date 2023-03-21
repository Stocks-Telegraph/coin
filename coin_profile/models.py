from django.db import models


class CoinProfile(models.Model):
    coin_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200, primary_key=True, unique=True)
    is_active = models.BooleanField(null=True)
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    started_at = models.DateField(auto_now=True)
    proof_type = models.CharField(max_length=200,null=True)
    org_structure = models.CharField(max_length=200, null=True)
    hash_algorithm = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name_plural = "Coin-Profile(all-coins)"
