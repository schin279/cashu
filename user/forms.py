from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    ROLES = (
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    )
    role = forms.ChoiceField(choices=ROLES)

    employee_first_name = forms.CharField(max_length=255, required=False)
    employee_last_name = forms.CharField(max_length=255, required=False)
    dob = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    employee_location = forms.CharField(max_length=255, required=False)
    
    employer_first_name = forms.CharField(max_length=255, required=False)
    employer_last_name = forms.CharField(max_length=255, required=False)
    company = forms.CharField(max_length=255, required=False)
    employer_location = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'role', 
            'employee_first_name', 
            'employee_last_name', 
            'dob', 
            'employee_location',
            'employer_first_name', 
            'employer_last_name',
            'company',
            'employer_location',
            ]

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        if role == 'employee':
            if not cleaned_data.get('employee_first_name') or not cleaned_data.get('employee_last_name') or not cleaned_data.get('dob') or not cleaned_data.get('employee_location'):
                raise forms.ValidationError('All employee fields are required.')
            return cleaned_data
        if role == 'employer':
            if not cleaned_data.get('employer_first_name') or not cleaned_data.get('employer_last_name') or not cleaned_data.get('company') or not cleaned_data.get('employer_location'):
                raise forms.ValidationError('All employer fields are required.')
            return cleaned_data

class PasswordResetForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)