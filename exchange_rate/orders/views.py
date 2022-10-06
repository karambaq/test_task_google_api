from django.shortcuts import render
from rest_framework import viewsets, mixins

from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


def index(request):
    return render(request, "index.html")
