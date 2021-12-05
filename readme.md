# README

## Init Project

```bash
docker-compose run web django-admin startproject web .

# if you running as the root, you should chown to user
chown -R $USER:$USER .

docker-compose up

docker exec django_web_1 python /code/manage.py migrate
# and createsuperuser
python manage.py createsuperuser
```

if there is any problem when you trying create super user, do this:
1. export your database config
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```
2. rerun manage.py in local
```bash
python manage.py createsuperuser

```

## Project Configuration
Reference:[django](https://docs.docker.com/samples/django/)
### Connect the database
In this section, you set up the database connection for Django.

In your project directory, edit the composeexample/settings.py file.

Replace the DATABASES = ... with the following:
```python
# settings.py
import os

[...]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
These settings are determined by the postgres Docker image specified in docker-compose.yml.

## Getting Start

```bash
# down all
docker-compose down -v
# up
docker-compose up
# specify db up
docker-compose up db
```

## Postgres Readonly User
```sql
CREATE USER readonly WITH PASSWORD 'readonly';
GRANT SELECT ON public.user TO readonly;

```

## Init sql
python3 model/user.py > config/init.sql 