# Generated by Django 5.0.4 on 2024-04-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_job_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
