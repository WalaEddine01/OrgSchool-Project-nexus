"""
Django forms for the OrgSchool application
Defines forms for admin registration, login, and CRUD for students, teachers, and classes.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import School, SClass, Student, Teacher
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

Admin = get_user_model()


class AdminRegistrationForm(UserCreationForm):
    """
    Registration form for school administrators.
    Extends Django's UserCreationForm.
    """
    email = forms.EmailField(required=True)
    school_name = forms.CharField(max_length=128, required=True)
    
    class Meta:
        model = Admin
        fields = ('username', 'email', 'school_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'school_name',
            'password1',
            'password2',
            Submit('submit', 'Sign Up', css_class='btn btn-primary')
        )
    
    def clean_email(self):
        # Ensure email is unique
        email = self.cleaned_data.get('email')
        if Admin.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
    
    def clean_school_name(self):
        # Ensure school name is unique
        school_name = self.cleaned_data.get('school_name')
        if Admin.objects.filter(school_name=school_name).exists():
            raise forms.ValidationError("That school name is taken. Please choose a different one.")
        return school_name
    
    def save(self, commit=True):
        # Save the admin and create the school
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.school_name = self.cleaned_data['school_name']
        if commit:
            user.save()
            # Create the school and default classes
            school = School.objects.create(
                name=user.school_name,
                admin=user
            )
            # Create 4 default classes
            for i in range(1, 5):
                SClass.objects.create(
                    name=f"Class 0{i}",
                    school=school
                )
        return user


class AdminLoginForm(AuthenticationForm):
    """
    Login form for administrators
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Login', css_class='btn btn-primary')
        )


class StudentForm(forms.ModelForm):
    """
    Form for creating/editing students
    """
    class Meta:
        model = Student
        fields = ['name', 'age', 'sclass']
    
    def __init__(self, *args, **kwargs):
        admin = kwargs.pop('admin', None)
        super().__init__(*args, **kwargs)
        if admin:
            # Filter classes by the admin's school
            self.fields['sclass'].queryset = SClass.objects.filter(school__admin=admin)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-8 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'sclass',
            Submit('submit', 'Save Student', css_class='btn btn-primary')
        )


class TeacherForm(forms.ModelForm):
    """
    Form for creating/editing teachers
    """
    class Meta:
        model = Teacher
        fields = ['name', 'sclass']
    
    def __init__(self, *args, **kwargs):
        admin = kwargs.pop('admin', None)
        super().__init__(*args, **kwargs)
        if admin:
            # Filter classes by the admin's school
            self.fields['sclass'].queryset = SClass.objects.filter(school__admin=admin)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'sclass',
            Submit('submit', 'Save Teacher', css_class='btn btn-primary')
        )


class SClassForm(forms.ModelForm):
    """
    Form for creating/editing classes
    """
    class Meta:
        model = SClass
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit('submit', 'Save Class', css_class='btn btn-primary')
        )
