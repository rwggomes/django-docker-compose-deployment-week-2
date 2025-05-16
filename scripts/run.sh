#!/bin/sh

# Exit on error
set -e

# Wait for the database to be ready
python manage.py wait_for_db

# Apply database migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000

