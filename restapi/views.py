"""
Django REST API views for the OrgSchool application
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from schools.models import Admin, School, SClass, Student, Teacher
from .serializers import (
    AdminSerializer, SchoolSerializer, SClassSerializer, 
    StudentSerializer, TeacherSerializer
)


class AdminViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Admin model (read-only)
    
    Provides read-only access to admin data. Users can only access their own admin information.
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own admin data
        return Admin.objects.filter(id=self.request.user.id)


class SchoolViewSet(viewsets.ModelViewSet):
    """
    ViewSet for School model
    
    Provides CRUD operations for schools. Users can only manage their own schools.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own schools
        return School.objects.filter(admin=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class SClassViewSet(viewsets.ModelViewSet):
    """
    ViewSet for SClass (School Class) model
    
    Provides CRUD operations for school classes. Users can only manage classes 
    from their own schools. Includes custom actions to get students and teachers.
    """
    queryset = SClass.objects.all()
    serializer_class = SClassSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see classes from their own schools
        return SClass.objects.filter(school__admin=self.request.user)
    
    def perform_create(self, serializer):
        # Ensure the class is created under the user's school
        school = School.objects.get(admin=self.request.user)
        serializer.save(school=school)
    
    @swagger_auto_schema(
        operation_description="Get all students in this class",
        responses={200: StudentSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        """
        Get all students in this class
        """
        sclass = self.get_object()
        students = Student.objects.filter(sclass=sclass)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Get all teachers in this class",
        responses={200: TeacherSerializer(many=True)}
    )
    @action(detail=True, methods=['get'])
    def teachers(self, request, pk=None):
        """
        Get all teachers in this class
        """
        sclass = self.get_object()
        teachers = Teacher.objects.filter(sclass=sclass)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Student model
    
    Provides CRUD operations for students. Users can only manage their own students.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own students
        return Student.objects.filter(admin=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class TeacherViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Teacher model
    
    Provides CRUD operations for teachers. Users can only manage their own teachers.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own teachers
        return Teacher.objects.filter(admin=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)
