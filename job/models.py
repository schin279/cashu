from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

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
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_jobs')
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    rating = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True)
    employer_rating = models.IntegerField(blank=True, null=True)
    employer_feedback = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return str(self.job_id)