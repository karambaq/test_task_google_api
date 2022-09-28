from rest_framework import viewsets, mixins

from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
