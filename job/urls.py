from django.urls import path
from .views import post_job, edit_job, delete_job, view_applications, review_application, accept_application, reject_application, employer_active_jobs, job_completed, job_list

urlpatterns = [
    path('post_job/', post_job, name='post_job'),
    path('employer/jobs/<int:job_id>/edit/', edit_job, name='edit_job'),
    path('employer/jobs/<int:job_id>/delete/', delete_job, name="delete_job"),
    path('employer/jobs/<int:job_id>/applications/', view_applications, name="view_applications"),
    path('employer/jobs/applications/<int:application_id>/', review_application, name="review_application"),
    path('employer/jobs/applications/<int:application_id>/accept/', accept_application, name="accept_application"),
    path('employer/jobs/applications/<int:application_id>/reject/', reject_application, name="reject_application"),
    path('employer/jobs/active/', employer_active_jobs, name="employer_active_jobs"),
    path('employer/jobs/active/<int:job_id>/complete/', job_completed, name="job_completed"),
    path('jobs/', job_list, name='job_list'),
]
