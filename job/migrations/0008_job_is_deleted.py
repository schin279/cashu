# Generated by Django 5.0.4 on 2024-04-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
