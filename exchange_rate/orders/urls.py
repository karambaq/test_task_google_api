from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, index

router = DefaultRouter()

router.register("orders", OrderViewSet, basename="orders")

urlpatterns = [
    path(
        "ordersi/",
        index,
    ),
    path("", include(router.urls)),
]
