from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' 
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),  # Adds date picker
        } # This includes all fields from Student model
