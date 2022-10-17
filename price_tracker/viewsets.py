from datetime import datetime

from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from django.urls import resolve
from .models import *
from .serializers import *


class CoinPriceViewset(viewsets.ModelViewSet):
    serializer_class = CoinPriceSerializer
    queryset = CoinPrice.objects.all()

    def get_queryset(self):
        coin_name = resolve(self.request.path_info).kwargs['coin_name']
        queryset = self.queryset.filter(coin=coin_name)
        if 'date' in self.request.query_params:
            date_query_param = self.request.query_params['date']
            queryset = queryset.filter(timestamp__date=datetime.strptime(date_query_param, "%Y/%m/%d"))
        return queryset
