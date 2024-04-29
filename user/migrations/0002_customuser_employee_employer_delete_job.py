# Generated by Django 5.0.4 on 2024-04-27 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('employerID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
