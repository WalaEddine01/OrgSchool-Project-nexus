"""
Django REST API views for the OrgSchool application
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Count
from schools.models import Admin, School, SClass, Student, Teacher
from .serializers import (
    AdminSerializer, SchoolSerializer, SClassSerializer, 
    StudentSerializer, TeacherSerializer
)


class AdminViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Admin model (read-only)
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
    ViewSet for SClass model
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
    
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        """
        Get all students in this class
        """
        sclass = self.get_object()
        students = Student.objects.filter(sclass=sclass)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
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
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own teachers
        return Teacher.objects.filter(admin=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class DashboardViewSet(viewsets.ViewSet):
    """
    ViewSet for dashboard statistics and data
    """
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """
        Get dashboard statistics
        """
        user = request.user
        
        # Get counts for user's data
        schools_count = School.objects.filter(admin=user).count()
        classes_count = SClass.objects.filter(school__admin=user).count()
        students_count = Student.objects.filter(admin=user).count()
        teachers_count = Teacher.objects.filter(admin=user).count()
        
        # Get detailed class statistics
        classes_with_counts = SClass.objects.filter(school__admin=user).annotate(
            student_count=Count('students'),
            teacher_count=Count('teachers')
        ).values('name', 'student_count', 'teacher_count')
        
        return Response({
            'total_schools': schools_count,
            'total_classes': classes_count,
            'total_students': students_count,
            'total_teachers': teachers_count,
            'class_details': list(classes_with_counts)
        })
    
    @action(detail=False, methods=['get'])
    def recent_activity(self, request):
        """
        Get recent activity data
        """
        user = request.user
        
        # Get recently added students and teachers
        recent_students = Student.objects.filter(admin=user).order_by('-created_at')[:5]
        recent_teachers = Teacher.objects.filter(admin=user).order_by('-created_at')[:5]
        
        student_data = StudentSerializer(recent_students, many=True).data
        teacher_data = TeacherSerializer(recent_teachers, many=True).data
        
        return Response({
            'recent_students': student_data,
            'recent_teachers': teacher_data
        })
