"""
Management command to create sample data for the OrgSchool application
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from schools.models import School, SClass, Student, Teacher

Admin = get_user_model()


class Command(BaseCommand):
    help = 'Create sample data for the OrgSchool application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--admin-email',
            type=str,
            default='admin@orgschool.com',
            help='Email for the admin user'
        )
        parser.add_argument(
            '--admin-password',
            type=str,
            default='admin123',
            help='Password for the admin user'
        )

    def handle(self, *args, **options):
        admin_email = options['admin_email']
        admin_password = options['admin_password']
        
        # Create admin user if it doesn't exist
        admin, created = Admin.objects.get_or_create(
            email=admin_email,
            defaults={
                'username': 'admin',
                'school_name': 'Demo School',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        
        if created:
            admin.set_password(admin_password)
            admin.save()
            self.stdout.write(
                self.style.SUCCESS(f'Created admin user: {admin_email}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Admin user already exists: {admin_email}')
            )
        
        # Create school
        school, created = School.objects.get_or_create(
            admin=admin,
            defaults={'name': admin.school_name}
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created school: {school.name}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'School already exists: {school.name}')
            )
        
        # Create classes
        classes_data = [
            'Class 01', 'Class 02', 'Class 03', 'Class 04'
        ]
        
        for class_name in classes_data:
            sclass, created = SClass.objects.get_or_create(
                name=class_name,
                school=school
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created class: {class_name}')
                )
        
        # Create sample students
        students_data = [
            {'name': 'John Doe', 'age': 10, 'class': 'Class 01'},
            {'name': 'Jane Smith', 'age': 11, 'class': 'Class 01'},
            {'name': 'Bob Johnson', 'age': 12, 'class': 'Class 02'},
            {'name': 'Alice Brown', 'age': 13, 'class': 'Class 02'},
            {'name': 'Charlie Wilson', 'age': 14, 'class': 'Class 03'},
            {'name': 'Eva Davis', 'age': 15, 'class': 'Class 03'},
            {'name': 'Frank Miller', 'age': 16, 'class': 'Class 04'},
            {'name': 'Grace Taylor', 'age': 17, 'class': 'Class 04'},
        ]
        
        for student_data in students_data:
            sclass = SClass.objects.get(name=student_data['class'], school=school)
            student, created = Student.objects.get_or_create(
                name=student_data['name'],
                admin=admin,
                defaults={
                    'age': student_data['age'],
                    'sclass': sclass,
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created student: {student.name}')
                )
        
        # Create sample teachers
        teachers_data = [
            {'name': 'Mr. Anderson', 'class': 'Class 01'},
            {'name': 'Ms. Thompson', 'class': 'Class 02'},
            {'name': 'Dr. Roberts', 'class': 'Class 03'},
            {'name': 'Prof. Williams', 'class': 'Class 04'},
        ]
        
        for teacher_data in teachers_data:
            sclass = SClass.objects.get(name=teacher_data['class'], school=school)
            teacher, created = Teacher.objects.get_or_create(
                name=teacher_data['name'],
                admin=admin,
                defaults={
                    'sclass': sclass,
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created teacher: {teacher.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write(
            f'Admin login: {admin_email} / {admin_password}'
        )
