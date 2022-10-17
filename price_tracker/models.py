from django.db import models


class CoinPrice(models.Model):
    timestamp = models.DateTimeField()
    price = models.FloatField()
    coin = models.CharField(max_length=13)
    currency = models.CharField(max_length=5)
