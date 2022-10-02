from datetime import datetime

from .constants import (
    NUM,
    ORDER_NUM,
    PRICE,
    DELIVERY_DATE,
)
from .utils import get_logger

logger = get_logger()


def is_valid_date(value) -> bool:
    "Checks if date is in fine format."
    try:
        dt = datetime.strptime(value, "%d.%m.%Y")
    except ValueError:
        logger.info(f"{value} can't be converted to date")
        return False
    # Can't predict the future
    return dt < datetime.today()


def is_valid_int_field(value) -> bool:
    "Checks if value from table can be converted to int and not negative."
    if not isinstance(value, int) or value <= 0:
        logger.info(f"{value} is not int or not positive.")
        return False
    return True


def is_valid_float_field(value) -> bool:
    "Check if value from table can be converted to float and not negative."
    try:
        float_value = float(value)
    except ValueError:
        logger.info(f"{value} is not convertable to float.")
        return False
    if float_value <= 0:
        logger.info(f"{float_value} is not positive.")
        return False
    return True


def validate_records(records) -> list[dict]:
    "Validates records from table and returns only valid ones."
    validated_records: list = []
    for record in records:
        logger.info(f"{record=}")
        # logger.info(f"{all(list(map(lambda x: x != '' record)))}")
        if not any(list(map(lambda x: x != "", record.values()))):
            logger.info("Empty line in table.")
            continue
        _id, order_id, price_usd, delivery_date = (
            record.get(NUM),
            record.get(ORDER_NUM),
            record.get(PRICE),
            record.get(DELIVERY_DATE),
        )
        if not all(
            [
                is_valid_int_field(_id),
                is_valid_int_field(order_id),
                is_valid_float_field(price_usd),
                is_valid_date(delivery_date),
            ]
        ):
            continue
        validated_records.append(record)
    return validated_records
