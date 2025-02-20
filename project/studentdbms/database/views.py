from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Student
from .forms import StudentForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json

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
def about(request):
    return render(request, "about.html")

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
