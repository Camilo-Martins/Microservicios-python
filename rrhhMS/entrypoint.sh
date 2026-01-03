#!/bin/sh
set -e

echo "Waiting for MySQL TCP at $HR_DB_HOST:$HR_DB_PORT..."

until nc -z "$HR_DB_HOST" "$HR_DB_PORT"; do
  echo "MySQL not ready yet..."
  sleep 2
done

echo "MySQL TCP is available!"

python manage.py makemigrations
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000