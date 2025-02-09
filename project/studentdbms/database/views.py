from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def database(request):
    """Handles form submission and saves student data to the database."""
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added to the database successfully!")
            return redirect('database')  # Redirect to the view page after saving

    return render(request, 'database.html', {'form': form})

def view(request):
    """Fetches and displays all student records."""
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})



