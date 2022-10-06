from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from ..serializers import OrderSerializer

from ..models import Order
from .google_api import get_worksheet
from .currency import fetch_rates_by_date
from .utils import convert_date_format, calculate_rub_price, get_logger
from .validators import validate_records
from .constants import (
    NUM,
    ORDER_NUM,
    PRICE,
    DELIVERY_DATE,
)
from .send_msg_to_tg import send_message_to_tg

logger = get_logger()
channel_layer = get_channel_layer()


def delete_old_orders(
    current_ids: set[int], validated_records: list[dict]
) -> None:
    """Find orders that was deleted from table and removing it"""
    # Using [] instead of `.get` because already validated
    current_nums = set(int(row[ORDER_NUM]) for row in validated_records)
    # Find orders which in the database but not in the table
    to_delete = current_ids - current_nums
    Order.objects.filter(order_id__in=to_delete).delete()


def is_delivery_outdated(date):
    "Template for 4.b task"
    return True


def update() -> None:
    "Updating database with new values"
    all_records: list[dict] = get_worksheet().get_all_records()
    validated_records = validate_records(all_records)

    current_order_ids = set(
        Order.objects.all().values_list("order_id", flat=True)
    )
    current_ids = set(Order.objects.all().values_list("id", flat=True))
    delete_old_orders(current_order_ids, validated_records)

    # Extracting all dates from table to make async requests
    current_dates: set[str | None] = set(
        row.get(DELIVERY_DATE) for row in validated_records
    )
    rates: dict[str, str] = fetch_rates_by_date(current_dates)

    orders_to_create: list = []
    orders_to_update: list = []
    for record in validated_records:
        # Using [] because already validated
        _id, order_id, price_usd, delivery_date = (
            record[NUM],
            record[ORDER_NUM],
            record[PRICE],
            record[DELIVERY_DATE],
        )

        # FYI: 4.b на счёт Телеграмма
        # "Если срок прошёл" - значит, что текущая дата больше срока поставки?
        # В таблице все даты раньше текущей, так что сделаю шаблон,
        # с дальнейшей возможностью переопределить нужное условие
        # is_delivery_late = is_delivery_outdated(delivery_date)
        # if is_delivery_late:
        #     send_message_to_tg(DELIVERY_LATE_MESSAGE.format(order_id)).delay()

        price_rub = calculate_rub_price(rates, delivery_date, price_usd)
        # Converting date to match django DateTime type.
        date = convert_date_format(delivery_date)
        order = Order(_id, order_id, price_usd, price_rub, date)
        # There is no bulk_create_or_update in Django,
        # so we need to check it first
        if _id not in current_ids and order_id not in current_order_ids:
            orders_to_create.append(order)
        else:
            orders_to_update.append(order)
    # Using bulk for better performance
    Order.objects.bulk_create(orders_to_create)
    Order.objects.bulk_update(
        orders_to_update,
        fields=["order_id", "price_usd", "price_rub", "delivery_date"],
    )
    serializer = OrderSerializer(Order.objects.all(), many=True)
    async_to_sync(channel_layer.group_send)(
        "orders",
        {"type": "send_new_data", "text": serializer.data},
    )
