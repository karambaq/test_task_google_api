from ..models import Order
from .google_api import get_worksheet
from .currency import fetch_rates_by_date
from .utils import convert_date_format


NUM = "№"
ORDER_NUM = "заказ №"
PRICE = "стоимость,$"
DELIVERY_DATE = "срок поставки"
COLUMN_NUM = 1
COLUMN_ORDER_NUM = 2
COLUMN_PRICE = 3
COLUMN_DELIVERY_DATE = 4


# TODO: Refactor into small methods
def update():
    ws = get_worksheet()
    all_records = ws.get_all_records()
    current_ids = set(Order.objects.all().values_list("order_id", flat=True))
    print(f"{current_ids=}")
    current_dates = set(row.get(DELIVERY_DATE) for row in all_records)
    print(current_dates)
    current_nums = set(int(row.get(ORDER_NUM)) for row in all_records)
    print(f"{current_nums=}")
    rates = fetch_rates_by_date(current_dates)
    to_delete = current_ids - current_nums
    print(f"{to_delete=}")
    Order.objects.filter(order_id__in=to_delete).delete()
    for row in all_records:
        _id, order_id, price_usd, delivery_date = (
            row.get(NUM),
            row.get(ORDER_NUM),
            row.get(PRICE),
            row.get(DELIVERY_DATE),
        )
        price_rub = rates.get(delivery_date)
        if price_rub is None:
            # print(f'There is no price for date: ')
            continue
        price_rub = float(price_rub.replace(",", "."))
        price_rub = price_rub * price_usd
        date = convert_date_format(delivery_date)
        # TODO: Try to bulk_create but keep in mind about updating
        order = Order(_id, order_id, price_usd, price_rub, date)
        order.save()
