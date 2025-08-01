# Migration Guide: Flask to Django

This document outlines the key changes made during the refactoring of OrgSchool from Flask to Django.

## Overview

The OrgSchool project has been completely refactored from Flask to Django while maintaining the same core functionality. The new Django version provides:

- Better structure and organization
- Built-in admin interface
- Professional REST API
- Enhanced security
- Better scalability

## File Structure Comparison

### Flask Version
```
├── app.py                    # Main Flask application
├── forms.py                  # WTForms forms
├── models/                   # SQLAlchemy models
│   ├── base_model.py
│   ├── admin.py
│   ├── school.py
│   ├── sclass.py
│   ├── student.py
│   └── teacher.py
├── api/v1/                   # Flask API
└── templates/                # Jinja2 templates
```

### Django Version
```
├── manage.py                 # Django management
├── orgschool_django/         # Project settings
├── schools/                  # Main Django app
│   ├── models.py            # Django models
│   ├── views.py             # Django views
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin configuration
│   └── urls.py              # URL routing
├── restapi/                  # REST API app
└── templates/schools/        # Django templates
```

## Key Changes

### 1. Models Migration

**Flask (SQLAlchemy)**:
```python
class Admin(BaseModel, UserMixin, Base):
    __tablename__ = 'admins'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    school_name = Column(String(128), nullable=False)
```

**Django**:
```python
class Admin(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    school_name = models.CharField(max_length=128)
    USERNAME_FIELD = 'email'
```

### 2. Views Migration

**Flask**:
```python
@app.route('/home')
def home():
    if current_user.is_authenticated:
        admin_id = current_user.id
        school = storage.get_by_key(School, 'admin_id', admin_id)
        return render_template('index.html', name=school.name)
    return render_template('index.html')
```

**Django**:
```python
def home_view(request):
    context = {}
    if request.user.is_authenticated:
        try:
            school = School.objects.get(admin=request.user)
            context['school_name'] = school.name
        except School.DoesNotExist:
            context['school_name'] = request.user.school_name
    return render(request, 'schools/index.html', context)
```

### 3. Forms Migration

**Flask (WTForms)**:
```python
class regestrationForm(FlaskForm):
    school_name = StringField('School Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
```

**Django**:
```python
class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    school_name = forms.CharField(max_length=128, required=True)
    
    class Meta:
        model = Admin
        fields = ('username', 'email', 'school_name', 'password1', 'password2')
```

### 4. API Migration

**Flask (Custom API)**:
```python
@app_views.route('/schools', methods=['GET'])
def get_schools():
    schools = storage.all(School).values()
    return jsonify([school.to_dict() for school in schools])
```

**Django (DRF)**:
```python
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]
```

### 5. URL Routing

**Flask**:
```python
@app.route('/')
@app.route("/about")
def about():
    return render_template('about.html')
```

**Django**:
```python
urlpatterns = [
    path('', views.about_view, name='about'),
    path('about/', views.about_view, name='about'),
]
```

## Database Schema Changes

The database schema remains largely the same, with these improvements:

1. **UUID Primary Keys**: All models now use UUID instead of auto-incrementing integers
2. **Better Relationships**: Improved foreign key constraints and relationships
3. **Custom User Model**: Uses Django's AbstractUser for better authentication

## Authentication Changes

- **Flask-Login** → **Django Authentication**
- **MD5 Password Hashing** → **Django's secure password hashing**
- **Session Management** → **Django's built-in session management**

## Template Changes

- **Jinja2** → **Django Template Language**
- **Flask template inheritance** → **Django template inheritance**
- **Bootstrap integration** → **Crispy Forms with Bootstrap 5**

## API Changes

- **Custom Flask API** → **Django REST Framework**
- **Manual serialization** → **DRF Serializers**
- **Custom authentication** → **DRF Authentication**

## Running Both Versions

You can run both versions side by side:

### Flask Version
```bash
# In the original directory
python app.py
# Runs on http://localhost:5000
```

### Django Version
```bash
# In the same directory
python manage.py runserver
# Runs on http://localhost:8000
```

## Benefits of the Django Version

1. **Better Structure**: Django's app-based structure provides better organization
2. **Admin Interface**: Built-in admin panel for data management
3. **Professional API**: Django REST Framework provides a production-ready API
4. **Security**: Django's built-in security features
5. **Scalability**: Better suited for large applications
6. **Community**: Larger community and ecosystem
7. **Documentation**: Comprehensive documentation and tutorials
8. **Testing**: Built-in testing framework
9. **Deployment**: Better deployment options and tools

## Migration Checklist

- [x] Models migrated to Django ORM
- [x] Views converted to Django views
- [x] Forms migrated to Django forms
- [x] Templates converted to Django templates
- [x] API rebuilt with Django REST Framework
- [x] Authentication system updated
- [x] Admin interface configured
- [x] URL routing updated
- [x] Static files configuration
- [x] Sample data creation
- [x] Documentation updated

## Next Steps

1. **Data Migration**: If you have existing data, create a migration script
2. **Testing**: Add comprehensive tests
3. **Production Setup**: Configure for production deployment
4. **Performance**: Add caching and optimization
5. **Features**: Add new features using Django's capabilities
