from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Attendance

admin.site.register(Student)
admin.site.register(Attendance)