# Generated by Django 5.0.4 on 2024-04-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]