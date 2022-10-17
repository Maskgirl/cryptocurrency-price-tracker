from rest_framework import serializers
from .models import *


class CoinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinPrice
        exclude = ('id', 'currency')
