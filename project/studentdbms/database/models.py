from django.db import models

class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ('MIT', 'MIT'),
        ('MLS', 'MLS'),
        ('TAPMI', 'TAPMI'),
        ('DLHS', 'DLHS'),
        ('DOC', 'DOC'),
        ('SMIT', 'SMIT'),
    ]

    COURSE_CHOICES = [
        ('CSE', 'CSE (Core)'),
        ('Cybersecurity', 'Cybersecurity'),
        ('AI', 'Artificial Intelligence'),
        ('DataScience', 'Data Science'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics & Communication'),
        ('VLSI', 'VLSI Design'),
        ('Other', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    email = models.EmailField(max_length=254, default="default@example.com")
    course = models.CharField(max_length=20, choices=COURSE_CHOICES, default='CSE')  # Dropdown
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)  # Allows values like 9.50
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, default='MIT')  # Dropdown

    def __str__(self):
        return self.name




