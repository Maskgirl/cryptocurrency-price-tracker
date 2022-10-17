from django.db import models


class CoinPrice(models.Model):
    timestamp = models.DateTimeField()
    price = models.IntegerField()
    coin = models.CharField(max_length=13)
    currency = models.CharField(max_length=5)
