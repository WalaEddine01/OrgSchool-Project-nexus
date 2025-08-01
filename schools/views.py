"""
Django views for the OrgSchool application
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import School, SClass, Student, Teacher, Admin
from .forms import AdminRegistrationForm, AdminLoginForm, StudentForm, TeacherForm, SClassForm


def api_docs_view(request):
    """
    API documentation view
    """
    return render(request, 'api_docs.html')


def about_view(request):
    """
    About page view
    """
    return render(request, 'schools/about.html')


def home_view(request):
    """
    Home page view with dashboard statistics
    """
    context = {}
    if request.user.is_authenticated:
        try:
            school = School.objects.get(admin=request.user)
            context['school_name'] = school.name
            
            # Get statistics
            context['total_classes'] = SClass.objects.filter(school=school).count()
            context['total_students'] = Student.objects.filter(admin=request.user).count()
            context['total_teachers'] = Teacher.objects.filter(admin=request.user).count()
            context['total_schools'] = School.objects.filter(admin=request.user).count()
            
        except School.DoesNotExist:
            context['school_name'] = request.user.school_name
            context['total_classes'] = 0
            context['total_students'] = Student.objects.filter(admin=request.user).count()
            context['total_teachers'] = Teacher.objects.filter(admin=request.user).count()
            context['total_schools'] = 0
    
    return render(request, 'index.html', context)


def register_view(request):
    """
    Registration view
    """
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}!')
            return redirect('schools:login')
    else:
        form = AdminRegistrationForm()
    return render(request, 'schools/register.html', {'form': form})


class ClassListView(LoginRequiredMixin, ListView):
    """
    List view for classes
    """
    model = SClass
    template_name = 'schools/class_list.html'
    context_object_name = 'classes'
    
    def get_queryset(self):
        try:
            school = School.objects.get(admin=self.request.user)
            return SClass.objects.filter(school=school)
        except School.DoesNotExist:
            return SClass.objects.none()


@login_required
def class_detail_view(request, class_id=None, class_name=None):
    """
    Detail view for a specific class
    """
    if class_id:
        sclass = get_object_or_404(SClass, id=class_id, school__admin=request.user)
    elif class_name:
        try:
            school = School.objects.get(admin=request.user)
            sclass = get_object_or_404(SClass, name=class_name, school=school)
        except School.DoesNotExist:
            sclass = None
    else:
        sclass = None
    
    if not sclass:
        messages.error(request, "Class not found or you don't have permission to view it.")
        return redirect('schools:class_list')
    
    students = Student.objects.filter(sclass=sclass)
    teachers = Teacher.objects.filter(sclass=sclass)
    
    context = {
        'sclass': sclass,
        'students': students,
        'teachers': teachers,
    }
    return render(request, 'schools/class_detail.html', context)


class StudentListView(LoginRequiredMixin, ListView):
    """
    List view for students
    """
    model = Student
    template_name = 'schools/student_list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        return Student.objects.filter(admin=self.request.user)


class StudentCreateView(LoginRequiredMixin, CreateView):
    """
    Create view for students
    """
    model = Student
    form_class = StudentForm
    template_name = 'schools/student_form.html'
    success_url = reverse_lazy('schools:student_list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['admin'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for students
    """
    model = Student
    form_class = StudentForm
    template_name = 'schools/student_form.html'
    success_url = reverse_lazy('schools:student_list')
    
    def get_queryset(self):
        return Student.objects.filter(admin=self.request.user)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['admin'] = self.request.user
        return kwargs


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete view for students
    """
    model = Student
    template_name = 'schools/student_confirm_delete.html'
    success_url = reverse_lazy('schools:student_list')
    
    def get_queryset(self):
        return Student.objects.filter(admin=self.request.user)


class TeacherListView(LoginRequiredMixin, ListView):
    """
    List view for teachers
    """
    model = Teacher
    template_name = 'schools/teacher_list.html'
    context_object_name = 'teachers'
    
    def get_queryset(self):
        return Teacher.objects.filter(admin=self.request.user)


class TeacherCreateView(LoginRequiredMixin, CreateView):
    """
    Create view for teachers
    """
    model = Teacher
    form_class = TeacherForm
    template_name = 'schools/teacher_form.html'
    success_url = reverse_lazy('schools:teacher_list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['admin'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for teachers
    """
    model = Teacher
    form_class = TeacherForm
    template_name = 'schools/teacher_form.html'
    success_url = reverse_lazy('schools:teacher_list')
    
    def get_queryset(self):
        return Teacher.objects.filter(admin=self.request.user)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['admin'] = self.request.user
        return kwargs


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete view for teachers
    """
    model = Teacher
    template_name = 'schools/teacher_confirm_delete.html'
    success_url = reverse_lazy('schools:teacher_list')
    
    def get_queryset(self):
        return Teacher.objects.filter(admin=self.request.user)


class ClassCreateView(LoginRequiredMixin, CreateView):
    """
    Create view for classes
    """
    model = SClass
    template_name = 'schools/class_form.html'
    fields = ['name']
    success_url = reverse_lazy('schools:class_list')
    
    def form_valid(self, form):
        try:
            school = School.objects.get(admin=self.request.user)
            form.instance.school = school
        except School.DoesNotExist:
            # Create a school if none exists
            school = School.objects.create(
                name=self.request.user.school_name,
                admin=self.request.user
            )
            form.instance.school = school
        return super().form_valid(form)
