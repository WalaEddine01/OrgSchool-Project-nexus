"""
Django models for the OrgSchool application
Defines Admin, School, SClass, Student, and Teacher models.
"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


class Admin(AbstractUser):
    """
    Custom user model for school administrators.
    Inherits from Django's AbstractUser and uses email as the username.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique admin ID
    email = models.EmailField(unique=True)  # Admin email (login)
    school_name = models.CharField(max_length=128)  # Name of the school
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)      # Last update timestamp
    
    # Use email as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'school_name']
    
    def __str__(self):
        return f"{self.school_name} Admin ({self.email})"


class School(models.Model):
    """
    School model. Each school is managed by an Admin.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique school ID
    name = models.CharField(max_length=128)  # School name
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='schools')  # Admin owner
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class SClass(models.Model):
    """
    School class model. Each class belongs to a school.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique class ID
    name = models.CharField(max_length=128)  # Class name
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='sclasses')  # Parent school
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
    
    def __str__(self):
        return f"{self.school.name} - {self.name}"


class Student(models.Model):
    """
    Student model. Each student belongs to a class and an admin.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique student ID
    name = models.CharField(max_length=128)  # Student name
    age = models.IntegerField()  # Student age
    sclass = models.ForeignKey(SClass, on_delete=models.CASCADE, related_name='students')  # Class
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='students')    # Admin owner
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.sclass.name})"


class Teacher(models.Model):
    """
    Teacher model. Each teacher belongs to a class and an admin.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique teacher ID
    name = models.CharField(max_length=128)  # Teacher name
    sclass = models.ForeignKey(SClass, on_delete=models.CASCADE, related_name='teachers')  # Class
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='teachers')    # Admin owner
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.sclass.name})"
