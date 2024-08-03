from django.contrib import admin

from django import forms
from .models import Hire_me


class HireMeAdmin(admin.ModelAdmin):
    list_display=(
        'company_name' ,
        'recruiter_name',
        'role',
        'post',
        'remote',
        'email',
        'salary',
        'currency',
    )

admin.site.register(Hire_me,HireMeAdmin)