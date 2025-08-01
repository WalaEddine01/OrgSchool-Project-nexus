#!/bin/bash

# OrgSchool Django Development Server Startup Script

echo "🎓 Starting OrgSchool Django Development Server..."
echo "=================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "⚠️  Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade requirements
echo "📦 Installing/updating requirements..."
pip install -r requirements.txt

# Run migrations
echo "🗄️  Running database migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python3 manage.py collectstatic --noinput

# Create superuser if needed
echo "👤 Checking for superuser..."
python3 manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    print('No superuser found. Please create one:')
    exit(1)
else:
    print('✅ Superuser already exists')
" || {
    echo "Creating superuser..."
    python3 manage.py createsuperuser
}

echo ""
echo "🚀 Starting Django development server..."
echo "📝 Access the application at: http://localhost:8000"
echo "⚙️  Access admin panel at: http://localhost:8000/admin"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Start the development server
python3 manage.py runserver 0.0.0.0:8000
