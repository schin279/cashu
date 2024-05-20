from django import forms
from .models import Job
from django.core.exceptions import ValidationError
import os

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'attachment', 'location', 'pay_rate', 'start_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the job title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter job details'}),
            'requirements': forms.Textarea(attrs={'placeholder': 'Enter skill requirements'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter job location'}),
            'pay_rate': forms.NumberInput(attrs={'placeholder': 'Enter the hourly rate'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.pdf', '.doc', '.docx']
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'File type not supported. (pdf, doc, docx only)')
    
    attachment = forms.FileField(label='Attachments', required=False, validators=[validate_file_extension])

    def clean_attachment(self):
        attachment = self.cleaned_data['attachment']
        if attachment:
            # Validate file extension
            extension = attachment.name.split('.')[-1].lower()
            if extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError('Only PDF, DOC, or DOCX files are allowed.')
            return attachment
        else:
            return None

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Job
        fields = ['rating', 'feedback']        