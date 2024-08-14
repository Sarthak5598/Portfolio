from django.shortcuts import render
from django.http import HttpResponse
from .models import Hire_me
from django.core.mail import send_mail

def home(request):
    return render(request,"base.html")

def work_experience(request):
    return render(request,"work_experience.html")

def projects(request):
    return render(request,'projects.html')

def stalk_me(request):
    return render(request,'omacare.html')

def hire_me(request):
    #TODO : ADD A Email system to send details to myself 
    if request.method == 'POST':
        # Extracting data from the request
        recruiter_name = request.POST.get('recruiter_name')
        company_name = request.POST.get('company_name')
        job_role = request.POST.get('job_role')
        post = request.POST.get('post')
        remote = request.POST.get('remote') == 'True'
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        currency = request.POST.get('currency')
        pay_type= request.POST.get('pay_type')

        # Save data to the database
        Hire_me.objects.create(
            recruiter_name=recruiter_name,
            company_name=company_name,
            role=job_role,
            post=post,
            remote=remote,
            email=email,
            salary=salary,
            currency=currency,
            pay_type=pay_type,
        )
        report_data = (
            "Hey, this is a weekly report from OWASP BLT regarding the bugs reported for your company!"
            f"\n\nRecruiter Name: {recruiter_name}"
            f"\nCompany Name: {company_name}"
            f"\nJob Role: {job_role}"
            f"\nJob Type: {post}"
            f"\nRemote: {'Yes' if remote else 'No'}"
            f"\nEmail: {email}"
            f"\nSalary: {salary} {currency} {pay_type}"
        )

        # # Send the report via email
        # send_mail(
        #     subject='Weekly Report from OWASP BLT',
        #     message=report_data,
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     [email],
        #     fail_silently=False,
        # )
        return render(request, 'hire_me.html', {'success': True})

    return render(request, 'hire_me.html')