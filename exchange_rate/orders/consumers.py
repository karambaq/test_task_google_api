from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Order
from .serializers import OrderSerializer


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        qs = await database_sync_to_async(self.get_orders)()
        await self.channel_layer.group_add("orders", self.channel_name)
        await self.accept()
        await self.send_new_data({"text": await self.serialize(qs)})

    def get_orders(self):
        return Order.objects.all()

    @sync_to_async
    def serialize(self, qs):
        return OrderSerializer(qs, many=True).data

    async def disconnect(self, code):
        await self.channel_layer.group_discard("orders", self.channel_name)

    async def send_new_data(self, event):
        new_data = event["text"]
        await self.send(json.dumps(new_data))
