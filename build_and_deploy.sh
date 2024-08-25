#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Step 2: Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Step 3: Run migrations (if needed)
echo "Running migrations..."
python manage.py migrate --noinput

# Step 4: Run Django server with hot reloading for development
echo "Starting Django server with hot reloading..."
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- python manage.py runserver

# Step 5: Deploy to Vercel (Optional, if you want to deploy)
# echo "Deploying to Vercel..."
# vercel --prod

echo "Development server with hot reloading started!"
