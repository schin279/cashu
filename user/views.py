from django.shortcuts import render, redirect
from .forms import CreateUserForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from job.models import Job
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from profiles.models import Employee_profile, Employer_profile

# Create your views here.
def home(request):
    jobs = Job.objects.filter(is_deleted=False, vacancies__gt=0)
    is_employee = request.user.is_authenticated and request.user.groups.filter(name='employee').exists()
    is_employer = request.user.is_authenticated and request.user.groups.filter(name='employer').exists()

    job_listings = Job.objects.none()
    
    if request.user.is_authenticated and is_employer:
        job_listings = Job.objects.filter(employer=request.user, is_deleted=False, vacancies__gt=0)
    
    # displays 5 most recent jobs
    recent_jobs = Job.objects.filter(is_deleted=False, vacancies__gt=0).order_by('-date_posted')[:5]
    
    # checks for already applied jobs (employees)
    applied_jobs = request.user.application_set.all().values_list('job_id', flat=True) if request.user.is_authenticated else []

    # displays job categories
    categories = Job.CATEGORY_CHOICES

    context = {'jobs': jobs, 'is_employee': is_employee, 'is_employer': is_employer, 'applied_jobs': applied_jobs, 'recent_jobs': recent_jobs, 'categories': categories, 'job_listings':job_listings}
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
                first_name = form.cleaned_data.get('employee_first_name')
                last_name = form.cleaned_data.get('employee_last_name')
                dob = form.cleaned_data.get('dob')
                location = form.cleaned_data.get('employee_location')
                Employee_profile.objects.create(user=user, first_name=first_name, last_name=last_name, dob=dob, location=location)
                
            elif role == 'employer':
                group = Group.objects.get(name='employer')
                first_name = form.cleaned_data.get('employer_first_name')
                last_name = form.cleaned_data.get('employer_last_name')
                company = form.cleaned_data.get('company')
                location = form.cleaned_data.get('employer_location')
                Employer_profile.objects.create(user=user, first_name=first_name, last_name=last_name, company=company, location=location)
            
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
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context={}
    return render(request, 'user/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def employer_jobs(request):
    is_employer = request.user.groups.filter(name='employer').exists()
    if is_employer:
        # view jobs posted
        jobs_posted = Job.objects.filter(employer=request.user, is_deleted=False)
        return render(request, 'employer/employer_jobs.html', {'jobs_posted': jobs_posted, 'is_employer': is_employer})
    else:
        return redirect('home')

@login_required(login_url='login')
def employee_profile(request):
    user = request.user
    is_employer = user.groups.filter(name='employer').exists()
    is_employee = user.groups.filter(name='employee').exists()

    if is_employee:
        active_jobs = Job.objects.filter(employee=user, is_active=True)
        completed_jobs = Job.objects.filter(employee=user, is_completed=True).exclude(employer_rating__isnull=True)
        return render(request, 'employee/employee_profile.html', {
            'is_employee': is_employee,
            'is_employer': is_employer,
            'employee': user, 
            'employee_profile':user.employee_profile,
            'employee_jobs': active_jobs,
            'jobs_done':completed_jobs,
        })
    else:
        return redirect('home')

@login_required(login_url='login')
def employer_profile(request):
    user = request.user
    is_employer = user.groups.filter(name='employer').exists()
    is_employee = user.groups.filter(name='employee').exists()

    if is_employer:
        active_jobs = Job.objects.filter(employer=user, is_active=True)
        completed_jobs = Job.objects.filter(employer=user, is_completed=True).exclude(employee_rating__isnull=True)
        return render(request, 'employer/employer_profile.html', {
            'is_employee': is_employee,
            'is_employer': is_employer,
            'employer': user, 
            'employer_profile':user.employer_profile,
            'employer_jobs': active_jobs,
            'jobs_done':completed_jobs,
        })
    else:
        return redirect('home')

@unauthenticated_user
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_password = form.cleaned_data['new_password']

            try:
                user = User.objects.get(username=username)

                # check if new password is same as old password
                if user.check_password(new_password):
                    messages.error(request, 'New password cannot be the same as previous password.')
                else:
                    # password validaiton
                    try:
                        validate_password(new_password, user=user)
                    except ValidationError as validation_errors:
                        for error in validation_errors:
                            messages.error(request, error)
                    else:
                        user.set_password(new_password)
                        user.save()
                        update_session_auth_hash(request, user)
                        messages.success(request, 'Password reset successful.')
                        return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'This username does not exist.')
        else:
            for errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = PasswordResetForm()
    
    return render(request, 'user/reset_password.html', {'form':form})

def view_employer_profile(request, username):
    try:
        user=User.objects.get(username=username)
        is_employee = user.groups.filter(name='employee').exists()
        is_employer = user.groups.filter(name='employer').exists()
        if is_employer:
            employer_profile = Employer_profile.objects.get(user=user)
            active_jobs = Job.objects.filter(employer=user, is_active=True)
            completed_jobs = Job.objects.filter(employer=user, is_completed=True).exclude(employee_rating__isnull=True)
            return render(request, 'employer/employer_profile.html', {
                'is_employee': is_employee,
                'is_employer': is_employer,
                'employer': user,
                'employer_profile': employer_profile,
                'employer_jobs': active_jobs,
                'jobs_done': completed_jobs,
            })
        else:
            messages.error(request, 'This user is not an employer.')
            return redirect('home')
    except User.DoesNotExist:
        messages.error(request, 'Employer not found.')
        return redirect('home')
    
def view_employee_profile(request, username):
    try:
        user=User.objects.get(username=username)
        is_employee = user.groups.filter(name='employee').exists()
        is_employer = user.groups.filter(name='employer').exists()
        if is_employee:
            employee_profile = Employee_profile.objects.get(user=user)
            active_jobs = Job.objects.filter(employee=user, is_active=True)
            completed_jobs = Job.objects.filter(employee=user, is_completed=True).exclude(employer_rating__isnull=True)
            return render(request, 'employee/employee_profile.html', {
                'is_employee': is_employee,
                'is_employer': is_employer,
                'employee': user,
                'employee_profile': employee_profile,
                'employee_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })
        else:
            messages.error(request, 'This user is not an employee.')
            return redirect('home')
    except User.DoesNotExist:
        messages.error(request, 'Employee not found.')
        return redirect('home')