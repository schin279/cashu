# Generated by Django 5.0.4 on 2024-05-27 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_employer_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer_profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employer_profile',
            name='last_name',
        ),
    ]
