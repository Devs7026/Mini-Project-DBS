from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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



