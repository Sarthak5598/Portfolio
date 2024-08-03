"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from port.views import (
    home,
    hire_me,
    work_experience,
    projects,
    stalk_me,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('hire-me/',hire_me,name='hire_me'),
    path('work-experience',work_experience,name='work_experience'),
    path('stalk-me/',stalk_me,name='stalk_me'),
    path('projects/',projects,name='projects')
]
