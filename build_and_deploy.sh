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

# Step 4: Deploy to Vercel
echo "Deploying to Vercel..."
vercel --prod

echo "Deployment completed successfully!"
