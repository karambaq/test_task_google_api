FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install postgresql-client openssl redis-server -y
RUN pip install poetry
ADD pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false \
    && poetry install  --no-interaction --no-ansi

COPY . .

# create user
RUN useradd -u 8877 admin
USER admin

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000