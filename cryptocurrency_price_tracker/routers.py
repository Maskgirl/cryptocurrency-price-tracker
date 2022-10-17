from rest_framework import routers
from price_tracker.viewsets import *

router = routers.DefaultRouter()

router.register(r'prices/(?P<coin_name>\w+)', CoinPriceViewset)
