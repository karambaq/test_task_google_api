from celery import shared_task

from .services import fill_db


@shared_task
def update_db():
    print("Updating database...")
    fill_db.update()
