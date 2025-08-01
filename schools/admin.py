"""
Django admin configuration for the OrgSchool application
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin, School, SClass, Student, Teacher


@admin.register(Admin)
class AdminUserAdmin(UserAdmin):
    """
    Admin configuration for the Admin model
    """
    list_display = ['username', 'email', 'school_name', 'is_staff', 'date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'school_name']
    
    fieldsets = UserAdmin.fieldsets + (
        ('School Information', {'fields': ('school_name',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('School Information', {'fields': ('email', 'school_name')}),
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    """
    Admin configuration for the School model
    """
    list_display = ['name', 'admin', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'admin__username', 'admin__email']


@admin.register(SClass)
class SClassAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SClass model
    """
    list_display = ['name', 'school', 'get_student_count', 'get_teacher_count', 'created_at']
    list_filter = ['school', 'created_at']
    search_fields = ['name', 'school__name']
    
    def get_student_count(self, obj):
        return obj.students.count()
    get_student_count.short_description = 'Students'
    
    def get_teacher_count(self, obj):
        return obj.teachers.count()
    get_teacher_count.short_description = 'Teachers'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Student model
    """
    list_display = ['name', 'age', 'sclass', 'admin', 'created_at']
    list_filter = ['age', 'sclass', 'created_at']
    search_fields = ['name', 'sclass__name', 'admin__username']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Teacher model
    """
    list_display = ['name', 'sclass', 'admin', 'created_at']
    list_filter = ['sclass', 'created_at']
    search_fields = ['name', 'sclass__name', 'admin__username']
