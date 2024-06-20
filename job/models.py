from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('IT', 'IT & Programming'),
        ('Design', 'Design & Creative'),
        ('Writing', 'Writing & Translation'),
        ('Admin', 'Admin Support'),
        ('Customer', 'Customer Support'),
        ('Sales', 'Sales & Marketing'),
        ('Other', 'Other'),
    ]

    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_jobs')
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    employee_rating = models.IntegerField(blank=True, null=True)
    employee_feedback = models.TextField(blank=True, null=True)
    employer_rating = models.IntegerField(blank=True, null=True)
    employer_feedback = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    vacancies = models.PositiveIntegerField(default=1)

    def get_status(self):
        if self.end_date and self.end_date <= timezone.now().date():
            return "Completed"
        else:
            return "Active"
        
    def has_vacancies(self):
        return self.vacancies > 0

    def __str__(self):
        return str(self.job_id)