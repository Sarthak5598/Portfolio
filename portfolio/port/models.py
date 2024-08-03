from django.db import models

# Create your models here.
JOB_TYPE_CHOICES = [
    ('Internship', 'Internship'),
    ('Full-time', 'Full-time'),
    ('Project-based', 'Project-based'),
]
PAY_TYPE_CHOICES =[
    ('/hr','/hr'),
    ('/project','/project'),
    ('/annum','/annum'),
]
class Hire_me(models.Model):
    company_name = models.CharField(max_length=100,null=True)
    recruiter_name = models.CharField(max_length=100,null=True)
    role = models.CharField(max_length=100,null=True)
    post = models.CharField(max_length=20,choices=JOB_TYPE_CHOICES,null=True)
    remote= models.BooleanField(default=False)
    email= models.EmailField(null=True)
    salary=models.CharField(max_length=200,null=True)
    pay_type=models.CharField(max_length=20,choices=PAY_TYPE_CHOICES,null=True)
    currency=models.CharField(max_length=20,null=True)

    
