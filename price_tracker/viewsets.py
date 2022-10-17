from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from .models import *
from .serializers import *


class CoinPriceViewset(viewsets.ModelViewSet):
    serializer_class = CoinPriceSerializer
    queryset = CoinPrice.objects.all()
