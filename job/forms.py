from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'location', 'rate']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Job
        fields = ['rating', 'feedback']        