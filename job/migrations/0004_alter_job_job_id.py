# Generated by Django 5.0.4 on 2024-04-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]