## Getting Started with Create React App

## Migrations and Static

`docker-compose run backend python3 manage.py migrate`

`docker-compose up -d`
`docker exec -it -u 0 backend python manage.py collectstatic --no-input`
