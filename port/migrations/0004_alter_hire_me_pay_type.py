# Generated by Django 5.0.7 on 2024-08-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_hire_me_pay_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire_me',
            name='pay_type',
            field=models.CharField(choices=[('/hr', '/hr'), ('/project', '/project'), ('/annum', '/annum')], max_length=20, null=True),
        ),
    ]
