from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import ApplicationForm

# Create your views here.

@login_required(login_url='login')
def apply(request, job_id):
    job = Job.objects.get(job_id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()

            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'employee/application.html', {'form': form, 'job': job})

@login_required(login_url='login')
def employee_applications(request):
    applications = Application.objects.filter(applicant=request.user).exclude(status__in=['Accepted', 'Rejected'])
    return render(request, 'employee/employee_applications.html', {'applications': applications})

@login_required(login_url='login')
def edit_application(request, application_id):
    application = get_object_or_404(Application, application_id=application_id, applicant=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            return redirect('employee_applications')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'employee/edit_application.html', {'form': form})

@login_required(login_url='login')
def delete_application(request, application_id):
    application = get_object_or_404(Application, application_id=application_id)
    if request.method == 'POST':
        application.delete()
        return redirect('employee_applications')
    return render(request, 'employee/delete_application.html', {'application': application})

@login_required(login_url='login')
def employee_active_jobs(request):
    active_jobs = Job.objects.filter(employee=request.user, is_active=True)
    return render(request, 'employee/active_jobs.html', {'employee_jobs':active_jobs})

@login_required(login_url='login')
def rate_employer(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')

        job.employer_rating = rating
        job.employer_feedback = feedback
        job.save()
        return redirect('employee_active_jobs')