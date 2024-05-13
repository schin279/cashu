"""Cashu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import home, signup, loginPage, logoutUser, employer_jobs, employee_profile, employer_profile
from job.views import post_job, edit_job, delete_job, view_applications, review_application, accept_application, reject_application, employer_active_jobs, job_completed, job_list
from applications.views import apply, employee_applications, edit_application, delete_application, employee_active_jobs, rate_employer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name="signup"),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('post_job/', post_job, name="post_job"),
    path('employer/jobs/', employer_jobs, name="employer_jobs"),
    path('employer/jobs/<int:job_id>/edit/', edit_job, name="edit_job"),
    path('employer/jobs/<int:job_id>/delete/', delete_job, name="delete_job"),
    path('employee/jobs/<int:job_id>/apply/', apply, name="apply"),
    path('employee/applications/', employee_applications, name="employee_applications"),
    path('employee/applications/<int:application_id>/edit/', edit_application, name="edit_application"),
    path('employee/application/<int:application_id>/delete/', delete_application, name="delete_application"),
    path('employer/jobs/<int:job_id>/applications/', view_applications, name="view_applications"),
    path('employer/jobs/applications/<int:application_id>/', review_application, name="review_application"),
    path('employer/jobs/applications/<int:application_id>/accept/', accept_application, name="accept_application"),
    path('employer/jobs/applications/<int:application_id>/reject/', reject_application, name="reject_application"),
    path('employer/jobs/active/', employer_active_jobs, name="employer_active_jobs"),
    path('employee/jobs/active/', employee_active_jobs, name="employee_active_jobs"),
    path('employer/jobs/active/<int:job_id>/complete/', job_completed, name="job_completed"),
    path('employee/profile/', employee_profile, name="employee_profile"),
    path('employee/jobs/<int:job_id>/rate/', rate_employer, name="rate_employer"),
    path('employer/profile/', employer_profile, name="employer_profile"),
    path('jobs/', job_list, name="job_list"),
]
