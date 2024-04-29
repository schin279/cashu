from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from job.models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.filter(is_deleted=False)
    is_employee = request.user.groups.filter(name='employee').exists()
    is_employer = request.user.groups.filter(name='employer').exists()

    # checks for already applied jobs (employees)
    applied_jobs = request.user.application_set.all().values_list('job_id', flat=True)
    
    context = {'jobs': jobs, 'is_employee': is_employee, 'is_employer': is_employer, 'applied_jobs': applied_jobs}
    return render(request, 'base/home.html', context)

@unauthenticated_user
def signup(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('role')

            if role == 'employee':
                group = Group.objects.get(name='employee')
            elif role == 'employer':
                group = Group.objects.get(name='employer')
            
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            
            return redirect('login')

    context = {'form':form}
    return render(request, 'user/signup.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.groups.filter(name='employee').exists():
                return redirect('employee_page')
            elif user.groups.filter(name='employer').exists():
                return redirect('employer_page')
            else:
                return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context={}
    return render(request, 'user/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def employee_page(request):
    is_employee = request.user.groups.filter(name='employee').exists()
    return render(request, 'employee/employee_page.html', {'is_employee': is_employee})

@login_required(login_url='login')
def employer_page(request):
    is_employer = request.user.groups.filter(name='employer').exists()
    if is_employer:
        return render(request, 'employer/employer_page.html', {'is_employer': is_employer})
    else:
        return redirect('home')
    
@login_required(login_url='login')
def employer_jobs(request):
    is_employer = request.user.groups.filter(name='employer').exists()
    if is_employer:
        # view jobs posted
        jobs_posted = Job.objects.filter(employer=request.user, is_deleted=False)
        return render(request, 'employer/employer_jobs.html', {'jobs_posted': jobs_posted})
    else:
        return redirect('home')

@login_required(login_url='login')
def employee_profile(request):
    employee = request.user
    active_jobs = Job.objects.filter(employee=employee, is_active=True)
    completed_jobs = Job.objects.filter(employee=employee, is_completed=True).exclude(rating__isnull=True)
    return render(request, 'employee/employee_profile.html', {'employee': employee, 'employee_jobs': active_jobs, 'completed_jobs':completed_jobs})

@login_required(login_url='login')
def employer_profile(request):
    employer = request.user
    active_jobs = Job.objects.filter(employer=employer, is_active=True)
    completed_jobs = Job.objects.filter(employer=employer, is_completed=True).exclude(rating__isnull=True)
    return render(request, 'employer/employer_profile.html', {'employer': employer, 'employer_jobs': active_jobs, 'jobs_done':completed_jobs})
