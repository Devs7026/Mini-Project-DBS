from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def database(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added to the database successfully!")
            return redirect('database')

    return render(request, 'database.html', {'form': form})

def view(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return JsonResponse({'success': True})


@csrf_exempt  # Disable CSRF for testing (use @csrf_protect in production)
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