from django import forms
from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        
        fields = ('emp_name', 'emp_email', 'emp_contact', 'emp_role', 'emp_salary', 'venue_image')

        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NOMBRE'}),
            'emp_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CORREO'}),
            'emp_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CONTACTO'}),
            'emp_role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ROL'}),
            'emp_salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SALARIO'}),
        }