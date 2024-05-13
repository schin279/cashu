from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateJobForm, ReviewForm
from .models import Job
from applications.models import Application

# Create your views here.

# job posting functionality (employer)
@login_required(login_url='login')
def post_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('employer_page')
    else:
        form = CreateJobForm()
    return render(request, 'employer/post_job.html', {'form': form})

# edit job posts (employer)
@login_required(login_url='login')
def edit_job(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    if request.method == 'POST':
        form = CreateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('employer_jobs')
    else:
        form = CreateJobForm(instance=job)
    return render(request, 'employer/edit_job.html', {'form': form})

# delete job posts (employer)
@login_required(login_url='login')
def delete_job(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    if request.method == 'POST':
        job.is_deleted = True
        job.save()
        return redirect('employer_jobs')
    return render(request, 'employer/delete_job.html', {'job': job})

def job_list(request):
    jobs = Job.objects.filter(is_deleted=False)
    is_employee = request.user.groups.filter(name='employee').exists()
    is_employer = request.user.groups.filter(name='employer').exists()

    # checks for already applied jobs (employees)
    applied_jobs = request.user.application_set.all().values_list('job_id', flat=True) if request.user.is_authenticated else []

    context = {'jobs': jobs, 'is_employee': is_employee, 'is_employer': is_employer, 'applied_jobs': applied_jobs}
    return render(request, 'base/job_list.html', context)

# view applications for jobs posted (employer)
@login_required(login_url='login')
def view_applications(request, job_id):
    job = get_object_or_404(Job, job_id=job_id, employer=request.user)
    applications = Application.objects.filter(job=job).exclude(status__in=['Accepted', 'Rejected'])
    return render(request, 'employer/view_applications.html', {'job': job, 'applications': applications})

# get application details for review (employer)
@login_required(login_url='login')
def review_application(request, application_id):
    application = get_object_or_404(Application, application_id=application_id)
    return render(request, 'employer/review_application.html', {'application': application})

# functionality to accept applications (employer)
@login_required(login_url='login')
def accept_application(request, application_id):
    application = get_object_or_404(Application, application_id=application_id)
    if application.job.employer == request.user:
        application.status = 'Accepted'
        application.save()
        
        # updates job status to active
        job = application.job
        job.is_active = True
        job.employee = application.applicant
        job.save()
    return redirect('view_applications', job_id=application.job.job_id)

# functionality to reject applications (employer)
@login_required(login_url='login')
def reject_application(request, application_id):
    application = get_object_or_404(Application, application_id=application_id)
    if application.job.employer == request.user:
        application.status = 'Rejected'
        application.save()
    return redirect('view_applications', job_id=application.job.job_id)

# updates job listing when application is accepted
@login_required(login_url='login')
def employer_jobs(request):
    jobs = Job.objects.filter(employer=request.user, is_deleted=False)
    jobs_posted = []
    for job in jobs:
        if not Application.objects.filter(job=job, status='Accepted').exists():
            jobs_posted.append(job)
    return render(request, 'employer/employer_jobs.html', {'jobs_posted': jobs_posted})

@login_required(login_url='login')
def employer_active_jobs(request):
    active_jobs = Job.objects.filter(employer=request.user, is_active=True, is_completed=False)
    return render(request, 'employer/active_jobs.html', {'active_jobs':active_jobs})

@login_required(login_url='login')
def job_completed(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')

        job.rating = rating
        job.feedback = feedback
        job.is_completed = True
        job.save()
        return redirect('employer_active_jobs')