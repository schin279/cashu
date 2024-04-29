from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    date_posted = models.DateField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_jobs')
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    rating = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True)
    employer_rating = models.IntegerField(blank=True, null=True)
    employer_feedback = models.TextField(blank=True)