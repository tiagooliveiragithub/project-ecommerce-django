#!/bin/sh
makemigrations.sh
echo 'A executar migrate.sh'
python manage.py migrate --noinput