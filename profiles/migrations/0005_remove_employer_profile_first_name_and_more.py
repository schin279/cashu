# Generated by Django 5.0.4 on 2024-05-27 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_employer_profile_first_name_and_more'),
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
