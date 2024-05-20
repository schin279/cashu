from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    ROLES = (
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    )
    role = forms.ChoiceField(choices=ROLES)

    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
    dob = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'first_name', 'last_name', 'dob', 'location']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        if role == 'employee':
            if not cleaned_data.get('first_name') or not cleaned_data.get('last_name') or not cleaned_data.get('dob') or not cleaned_data.get('location'):
                raise forms.ValidationError('All employee fields are required.')
            return cleaned_data

class PasswordResetForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)