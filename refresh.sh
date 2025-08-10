#!/bin/bash

# Set path to the .env file
ENV_FILE=".env"
ROOT_PASS="wala"

# Check if .env file exists
if [[ ! -f "$ENV_FILE" ]]; then
    echo "❌ .env file not found at $ENV_FILE"
    exit 1
fi

# Load environment variables from .env
export $(grep -v '^#' "$ENV_FILE" | xargs)

echo "✅ Loaded .env variables"
echo "🔐 SECRET_KEY: ${SECRET_KEY:0:5}..."
echo "🌐 DATABASE_URL: $DATABASE_URL"

# Parse DATABASE_URL

echo "🔍 Database details:"
echo "  User: $DB_USER"
echo "  Database: $DB_NAME"
echo "  Host: $DB_HOST:$DB_PORT"



# Drop and recreate the database
echo "🗑️ Dropping and recreating database: $DB_NAME"
mysql -u root -p"$ROOT_PASS" -h "$DB_HOST" -P "$DB_PORT" <<EOF
DROP DATABASE IF EXISTS $DB_NAME;
CREATE DATABASE $DB_NAME CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';
FLUSH PRIVILEGES;
EOF

if [ $? -ne 0 ]; then
    echo "❌ Failed to recreate database"
    exit 1
fi

echo "✅ Database recreated successfully"

# Clean old migrations and cache
echo "🧹 Cleaning old migration files and cache..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# Ensure migrations directory exists
mkdir -p tasks/migrations
touch tasks/migrations/__init__.py

# Check Django configuration
echo "🔍 Checking Django configuration..."

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py shell <<EOF
from django.contrib.auth import get_user_model
import traceback
User = get_user_model()
User.objects.create_superuser('wala', 'wala@example.com', 'wala')
EOF

