from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Student, Attendance
from .forms import StudentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, date
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home/") 
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "login.html")  


@login_required
def home(request):
    return render(request, "index.html")

@login_required
def database(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('database')

    return render(request, 'database.html', {'form': form})

@login_required
def view(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})

@login_required
def attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        attendance_date_str = request.POST.get('attendanceDate')
        if attendance_date_str:
            attendance_date = datetime.strptime(attendance_date_str, '%Y-%m-%d').date()
        else:
            messages.error(request, "Please select a date.")
            return render(request, 'attendance.html', {'students': students})

        for student in students:
            present = request.POST.get(f'attendance_{student.id}') == 'present'
            try:
                # Get or create the attendance record for the student and date
                attendance = Attendance.objects.create(
                    student=student,
                    date=attendance_date,
                    present=present
                )
            except IntegrityError as e:
                messages.warning(request, f"Attendance already recorded for {student.name} on {attendance_date}.  Skipping.")


        messages.success(request, "Attendance submitted successfully!")
        return redirect('attendance')  # Redirect to refresh the page
    else:
        # Calculate attendance percentage for each student
        for student in students:
            total_days = Attendance.objects.filter(student=student).count()
            present_days = Attendance.objects.filter(student=student, present=True).count()

            if total_days > 0:
                percentage = (present_days / total_days) * 100
            else:
                percentage = 0.0  # Or some other default value, like None or -1

            student.attendance_percentage = round(percentage, 2)  # Store percentage in student object for template

        # Fetch all attendance records for display
        all_attendance = Attendance.objects.all()


        return render(request, "attendance.html", {'students': students, 'all_attendance': all_attendance})

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return JsonResponse({'success': True})

@csrf_exempt
@login_required
def update_student(request, student_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = Student.objects.get(id=student_id)
            student.name = data["name"]
            student.email = data["email"]
            student.dob = data["dob"]
            student.course = data["course"]
            student.cgpa = data["cgpa"]
            student.save()
            return JsonResponse({"success": True})
        except Student.DoesNotExist:
            return JsonResponse({"success": False, "error": "Student not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})






