from django.db import models
from django.contrib.auth.models import User
from job.models import Job

# Create your models here.

class Application(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    application_id = models.AutoField(primary_key=True, default=None)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')