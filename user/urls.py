from django.shortcuts import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('employer/jobs/',views.employer_jobs, name="employer_jobs"),
    path('employee/profile/', views.employee_profile, name="employee_profile"),
    path('employer/profile/', views.employer_profile, name="employer_profile"),
]
