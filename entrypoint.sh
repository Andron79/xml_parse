#!/bin/sh

until pg_isready -h "$POSTGRES_HOST"; do
  echo "Waiting for database start..."
  sleep 1
done

python manage.py makemigrations
python manage.py migrate
#./fixtures.sh load
python manage.py runserver 0.0.0.0:8000