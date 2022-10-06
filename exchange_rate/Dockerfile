FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code
#    openldap \
#    libcurl \
RUN apk update && apk upgrade
RUN apk add --no-cache gcc \
    libc-dev \
    && rm -rf /var/cache/apk/*
RUN pip install poetry
ADD pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false \
    && poetry install  --no-interaction --no-ansi

COPY . .


# EXPOSE 8000
# CMD python manage.py runserver 0.0.0.0:8000
# CMD gunicorn --workers=4 --threads=3 exchange_rate.wsgi:application --bind 0.0.0.0:8000
CMD daphne -b 0.0.0.0 -p 8000 exchange_rate.asgi:application 