# OrgSchool - Django Version

A modern school management system built with Django and Django REST Framework. This is a complete refactored version of the original Flask-based OrgSchool application.

## Features

- **User Authentication**: Custom user model for school administrators
- **School Management**: Create and manage schools
- **Class Management**: Organize students into different classes
- **Student Management**: Track student information including name, age, and class assignments
- **Teacher Management**: Assign teachers to classes and maintain records
- **REST API**: Full REST API with Django REST Framework
- **Admin Interface**: Django admin panel for advanced management
- **Responsive UI**: Modern Bootstrap-based interface

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (default), MySQL supported
- **API**: Django REST Framework
- **Frontend**: Bootstrap 5, Crispy Forms
- **Authentication**: Django's built-in authentication system

## Project Structure

```
/home/wala/OrgSchool-Project-nexus2/
├── manage.py                 # Django management script
├── orgschool_django/         # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Main settings file
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── schools/                  # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View functions and classes
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin configuration
│   ├── urls.py              # App URL configuration
│   └── management/commands/ # Custom management commands
├── restapi/                  # REST API app
│   ├── views.py             # API viewsets
│   ├── serializers.py       # API serializers
│   └── urls.py              # API URL configuration
├── templates/schools/        # Django templates
├── static/                   # Static files (CSS, JS, images)
└── requirements_django.txt   # Python dependencies
```

## Installation and Setup

### 1. Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### 2. Install Dependencies
```bash
# Install Django dependencies
pip install -r requirements_django.txt
```

### 3. Database Setup
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create sample data (optional)
python manage.py create_sample_data
```

### 4. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Web Interface

1. **Homepage**: Visit `http://127.0.0.1:8000/` to see the landing page
2. **Register**: Create a new school administrator account
3. **Login**: Access your school dashboard
4. **Manage**: Use the web interface to manage classes, students, and teachers

### Admin Interface

Visit `http://127.0.0.1:8000/admin/` to access the Django admin panel.

Default admin credentials (if using sample data):
- Email: `admin@orgschool.com`
- Password: `admin123`

### REST API

The REST API is available at `http://127.0.0.1:8000/api/v1/`

#### Available Endpoints:

- `/api/v1/admins/` - Admin users (read-only)
- `/api/v1/schools/` - Schools
- `/api/v1/sclasses/` - Classes
- `/api/v1/students/` - Students
- `/api/v1/teachers/` - Teachers

#### API Authentication

The API uses session-based authentication. You need to be logged in through the web interface to access the API.

#### Example API Usage:

```bash
# Get all students (requires authentication)
curl -X GET http://127.0.0.1:8000/api/v1/students/ \
  -H "Cookie: sessionid=your_session_id"

# Create a new student
curl -X POST http://127.0.0.1:8000/api/v1/students/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=your_session_id" \
  -d '{
    "name": "New Student",
    "age": 15,
    "sclass": "class_uuid_here"
  }'
```

## Key Differences from Flask Version

### 1. Models
- **Django ORM**: Replaced SQLAlchemy with Django's ORM
- **UUID Primary Keys**: All models use UUID primary keys
- **Custom User Model**: Uses Django's AbstractUser for administrators
- **Better Relationships**: Improved foreign key relationships

### 2. Views
- **Class-Based Views**: Utilizes Django's generic views for CRUD operations
- **Function-Based Views**: For custom logic and compatibility
- **Built-in Authentication**: Uses Django's authentication decorators

### 3. Forms
- **Django Forms**: Replaced WTForms with Django forms
- **Crispy Forms**: Enhanced form rendering with Bootstrap styling
- **Validation**: Built-in Django form validation

### 4. Templates
- **Django Template Language**: Replaced Jinja2 with Django templates
- **Bootstrap 5**: Modern responsive design
- **Template Inheritance**: Better template organization

### 5. API
- **Django REST Framework**: Professional REST API implementation
- **Viewsets**: Automatic CRUD operations
- **Serializers**: Proper data serialization
- **Browsable API**: Built-in API documentation

### 6. Administration
- **Django Admin**: Powerful built-in admin interface
- **Custom Admin**: Customized admin panels for all models
- **User Management**: Built-in user management system

## Configuration

### Database Configuration

By default, the application uses SQLite. To use MySQL, update the `DATABASES` setting in `orgschool_django/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orgschool_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Environment Variables

You can use environment variables for sensitive settings:

```bash
export SECRET_KEY='your-secret-key'
export DEBUG=False
export DATABASE_URL='mysql://user:password@localhost/dbname'
```

## Development

### Running Tests
```bash
python manage.py test
```

### Creating New Migrations
```bash
python manage.py makemigrations schools
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## Production Deployment

For production deployment, consider:

1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL recommended)
3. Use a production web server (Gunicorn + Nginx)
4. Set up proper static file serving
5. Configure environment variables for sensitive data
6. Set up SSL/HTTPS

## Migration from Flask Version

If you're migrating data from the Flask version:

1. Export data from the Flask application
2. Create a custom Django management command to import the data
3. Map the SQLAlchemy models to Django models
4. Run the import command

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## License

This project maintains the same license as the original Flask version.

## Support

For issues and questions:
1. Check the Django documentation
2. Review the original Flask version for business logic reference
3. Create an issue in the repository

## Credits

This Django version is a complete refactor of the original Flask-based OrgSchool application, maintaining the same core functionality while leveraging Django's powerful features and conventions.
