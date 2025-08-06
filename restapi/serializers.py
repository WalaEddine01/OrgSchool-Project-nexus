"""
Django REST API serializers for the OrgSchool application
Defines serializers for Admin, School, SClass, Student, and Teacher models.
"""
from rest_framework import serializers
from schools.models import Admin, School, SClass, Student, Teacher


class AdminSerializer(serializers.ModelSerializer):
    """
    Serializes Admin model for API output.
    """
    class Meta:
        model = Admin
        fields = ['id', 'username', 'email', 'school_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class SchoolSerializer(serializers.ModelSerializer):
    """
    Serializes School model. Includes admin email for reference.
    """
    admin_email = serializers.EmailField(source='admin.email', read_only=True)
    
    class Meta:
        model = School
        fields = ['id', 'name', 'admin', 'admin_email', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class SClassSerializer(serializers.ModelSerializer):
    """
    Serializes SClass model. Adds school name and student/teacher counts.
    """
    school_name = serializers.CharField(source='school.name', read_only=True)
    student_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    
    class Meta:
        model = SClass
        fields = ['id', 'name', 'school', 'school_name', 'student_count', 'teacher_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_student_count(self, obj):
        # Return number of students in class
        return obj.students.count()
    
    def get_teacher_count(self, obj):
        # Return number of teachers in class
        return obj.teachers.count()


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializes Student model. Adds class and school names.
    """
    sclass_name = serializers.CharField(source='sclass.name', read_only=True)
    school_name = serializers.CharField(source='sclass.school.name', read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sclass', 'sclass_name', 'school_name', 'admin', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializes Teacher model. Adds class and school names.
    """
    sclass_name = serializers.CharField(source='sclass.name', read_only=True)  # Class name
    school_name = serializers.CharField(source='sclass.school.name', read_only=True)  # School name
    
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'sclass', 'sclass_name', 'school_name', 'admin', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
