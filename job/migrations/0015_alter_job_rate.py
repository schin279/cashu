# Generated by Django 5.0.4 on 2024-05-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_rename_employr_feedback_job_employer_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
