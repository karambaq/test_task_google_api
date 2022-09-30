import os

import telegram
from celery import shared_task  # type: ignore

from .utils import get_logger


logger = get_logger()


@shared_task
def send_message_to_tg(message):
    logger.info(f"Trying to send message {message}")
    try:
        bot = telegram.Bot(os.getenv("TG_TOKEN"))
        bot.send_message(
            os.getenv("CHANNEL_ID"),
            message,
            disable_web_page_preview=True,
            parse_mode=telegram.ParseMode.MARKDOWN,
        )
    except Exception as ex:
        logger.error(f"Exception of type {type(ex).__name__} in (): {str(ex)}")
    finally:
        logger.info("Finished sending.")
