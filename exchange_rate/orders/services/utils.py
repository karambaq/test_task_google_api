from datetime import datetime
import logging
import sys


def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%d.%m.%y %H:%M:%S",
        format="%(asctime)s [%(filename)s:%(lineno)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logger = logging.getLogger()
    return logger


logger = get_logger()


def convert_date_format(date: str) -> str:
    "Converting date from table to match django DateTime field."
    dt = datetime.strptime(date, "%d.%m.%Y")
    return dt.strftime("%Y-%m-%d")


def calculate_rub_price(
    rates: dict[str, str], delivery_date: str, price_usd: float
) -> float:
    "Gets rub rate for usd and multiplies with usd amount."
    usd_to_rub_rate = rates.get(delivery_date)
    if usd_to_rub_rate is None:
        logger.info(f"There is no usd_rate for this date: {delivery_date} ")
        return 0
    # There is ',' in table so we need to replace it with '.'
    float_usd_rate = float(usd_to_rub_rate.replace(",", "."))
    return float_usd_rate * price_usd
