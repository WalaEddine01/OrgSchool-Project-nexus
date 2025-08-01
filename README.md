# 🎓 OrgSchool - Modern School Management System

A comprehensive Django-based school management system designed to streamline educational administration with a modern, responsive interface.

## ✨ Features

- **Student Management**: Complete student profiles, enrollment tracking, and progress monitoring
- **Teacher Administration**: Efficient teacher scheduling and assignment management
- **Class Organization**: Streamlined class creation and student assignments
- **Modern UI**: Beautiful, responsive design built with Bootstrap 5
- **REST API**: Full API integration for external applications
- **Security**: Enterprise-grade security with role-based access control
- **Mobile Responsive**: Works seamlessly on all devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd OrgSchool-Project-nexus
```

2. **Run the development server**
```bash
./run_dev_server.sh
```

The script will automatically:
- Create a virtual environment
- Install dependencies
- Run database migrations
- Collect static files
- Start the development server

3. **Access the application**
- Main application: http://localhost:8000
- Admin panel: http://localhost:8000/admin

### Manual Setup (Alternative)

If you prefer manual setup:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser

# Start development server
python3 manage.py runserver
```

## 🏗️ Project Structure

```
OrgSchool-Project-nexus/
├── manage.py                 # Django management script
├── requirements.txt         # Python dependencies
├── run_dev_server.sh       # Development server startup script
├── db.sqlite3              # SQLite database (development)
│
├── orgschool_django/       # Main project settings
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
│
├── schools/                # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions/classes
│   ├── urls.py            # URL patterns
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin interface configuration
│   └── migrations/        # Database migrations
│
├── restapi/               # REST API application
│   ├── views.py           # API views
│   ├── serializers.py     # API serializers
│   └── urls.py            # API URL patterns
│
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── about.html         # About page
│   └── schools/           # School-specific templates
│
└── static/                # Static files (CSS, JS, images)
    └── css/
        └── modern-style.css  # Custom CSS styles
```

## 🎨 Technology Stack

- **Backend**: Django 5.x (Python web framework)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **API**: Django REST Framework
- **Authentication**: Django's built-in authentication system
- **Icons**: Font Awesome 6
- **Fonts**: Inter (Google Fonts)

## 📱 Features Overview

### Dashboard
- Interactive statistics cards
- Quick action buttons
- Modern gradient design
- Mobile-responsive layout

### Student Management
- Add, edit, and delete student records
- Assign students to classes
- Track academic progress
- Search and filter capabilities

### Teacher Management
- Teacher profile management
- Class assignments
- Contact information
- Performance tracking

### Class Organization
- Create and manage classes
- View class rosters
- Teacher assignments
- Student-teacher relationships

### Authentication
- Secure login/logout system
- User registration
- Role-based permissions
- Session management

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Configuration

For production, update `DATABASES` in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'orgschool_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Deployment

### Production Checklist

1. Set `DEBUG = False` in settings
2. Configure proper database (PostgreSQL/MySQL)
3. Set up static file serving with WhiteNoise or CDN
4. Configure environment variables
5. Set up SSL/HTTPS
6. Configure backup strategy

### Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "orgschool_django.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

See [AUTHORS](AUTHORS) file for a list of contributors.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Email: support@orgschool.com
- Documentation: [Link to docs]

## 🔄 Changelog

### Version 2.0.0 (Current)
- Migrated from Flask to Django
- Modern Bootstrap 5 UI
- REST API integration
- Mobile-responsive design
- Enhanced security features
- Improved admin interface

### Version 1.0.0
- Initial Flask implementation
- Basic CRUD operations
- Simple UI design

---

**OrgSchool** - Empowering educational institutions with modern management solutions.
