from django.shortcuts import render
from django.http import HttpResponse
from .models import Hire_me

def home(request):
    return render(request,"base.html")

def work_experience(request):
    return render(request,"work_experience.html")

def projects(request):
    return render(request,'projects.html')

def stalk_me(request):
    return render(request,'stalk_me.html')

def hire_me(request):
    if request.method == 'POST':
        # Extracting data from the request
        recruiter_name = request.POST.get('recruiter_name')
        company_name = request.POST.get('company_name')
        job_role = request.POST.get('job_role')
        post = request.POST.get('post')
        remote = request.POST.get('remote') == 'True'  # Convert string to boolean
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        currency = request.POST.get('currency')

        # Save data to the database
        Hire_me.objects.create(
            recruiter_name=recruiter_name,
            company_name=company_name,
            role=job_role,
            post=post,
            remote=remote,
            email=email,
            salary=salary,
            currency=currency
        )

        return render(request, 'hire_me.html', {'success': True})

    return render(request, 'hire_me.html')