from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
