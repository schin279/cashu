# Generated by Django 5.0.4 on 2024-06-02 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0021_job_vacancies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='feedback',
            new_name='employee_feedback',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='rating',
            new_name='employee_rating',
        ),
    ]
