FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install poetry
ADD pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false \
    && poetry install  --no-interaction --no-ansi

COPY . .


# EXPOSE 8000
# CMD python manage.py runserver 0.0.0.0:8000
CMD gunicorn --workers=4 --threads=3 exchange_rate.wsgi:application --bind 0.0.0.0:8000