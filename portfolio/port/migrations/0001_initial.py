# Generated by Django 5.0.7 on 2024-07-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hire_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('recruiter_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('post', models.CharField(choices=[('Internship', 'Internship'), ('Full-time', 'Full-time'), ('Project-based', 'Project-based')], max_length=20)),
                ('remote', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=20)),
            ],
        ),
    ]
