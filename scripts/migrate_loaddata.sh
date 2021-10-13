#!/usr/bin/env bash

# run migrations
echo "Running migrations..."
python manage.py showmigrations
python manage.py migrate
python manage.py showmigrations

# load default data
echo "Creating default user..."
python manage.py createdefaultsuperuser

# echo "Creating default service configs..."
python manage.py createdefaultconfigs

# collect static
echo "Collecting static files..."
python manage.py collectstatic --noinput
