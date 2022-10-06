from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    price_rub = serializers.SerializerMethodField()
    price_usd = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_price_rub(self, obj):
        return float(obj.price_rub or 0)

    def get_price_usd(self, obj):
        return float(obj.price_usd)
