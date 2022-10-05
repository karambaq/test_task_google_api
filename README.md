## Instruction to launch

- `git clone https://github.com/karambaq/test_task_google_api`

- `cd test_task_google_api`
- `touch .env`

Fill it with

```
SHEET_NAME=Лист1
DB_NAME=postgres
DB_USER=postgres
DB_HOST=db
DB_PORT=5432
SHEET_URL=https://docs.google.com/spreadsheets/d/17PynPkgYnd1XwUEzWZ6fRNi3fw5IZIBmKqTfwmAPonQ/edit#gid=0
SECRET_KEY=SOME_KEY
```

## Migrations and Static

- `docker-compose run backend python3 manage.py migrate`

- `docker-compose up -d`

- `docker exec -it -u 0 backend python manage.py collectstatic --no-input`

# Launch

- `docker-compose up --build -d`

Then navigate to `localhost` in browser

# Google Sheet link:

https://docs.google.com/spreadsheets/d/17PynPkgYnd1XwUEzWZ6fRNi3fw5IZIBmKqTfwmAPonQ/edit#gid=0

# Author

@karambaq
