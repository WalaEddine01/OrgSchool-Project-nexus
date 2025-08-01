"""
URL configuration for the schools app
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'schools'

urlpatterns = [
    # Public pages
    path('', views.about_view, name='about'),
    path('about/', views.about_view, name='about'),
    path('home/', views.home_view, name='home'),
    path('api-docs/', views.api_docs_view, name='api_docs'),
    
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='schools/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Classes
    path('classes/', views.ClassListView.as_view(), name='class_list'),
    path('classes/add/', views.ClassCreateView.as_view(), name='class_create'),
    path('class/<uuid:class_id>/', views.class_detail_view, name='class_detail'),
    
    # Students
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<uuid:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<uuid:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    
    # Teachers
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/add/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<uuid:pk>/edit/', views.TeacherUpdateView.as_view(), name='teacher_edit'),
    path('teachers/<uuid:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
]
