from rest_framework import routers
from price_tracker.viewsets import *

router = routers.DefaultRouter()

router.register('prices/bitcoin', CoinPriceViewset)
