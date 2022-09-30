from celery import shared_task

from .services import fill_db
from .services import utils

logger = utils.get_logger()


@shared_task
def update_db():
    logger.info("Updating database...")
    fill_db.update()
