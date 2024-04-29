from django.urls import path
from .views import apply, employee_applications, edit_application, delete_application, employee_active_jobs, rate_employer

urlpatterns = [
    path('employee/jobs/<int:job_id>/apply/', apply, name="apply"),
    path('employee/applications/', employee_applications, name="employee_applications"),
    path('employee/applications/<int:application_id>/edit', edit_application, name="edit_application"),
    path('employee/applications/<int:application_id>/delete/', delete_application, name="delete_application"),
    path('employee/jobs/active/', employee_active_jobs, name="employee_active_jobs"),
    path('employee/jobs/<int:job_id>/rate/', rate_employer, name="rate_employer"),
]
