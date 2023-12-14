#!/bin/sh

# Change to the app directory
cd /Albion_Market_DYD_Django

# Apply database migrations
echo "Applying database migrations"
python manage.py makemigrations
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Start the server using gunicorn
echo "Starting the server"
gunicorn drf_kubernetes.wsgi:application --bind 0.0.0.0:8000