# Generated by Django 5.0.4 on 2024-04-29 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='id',
        ),
        migrations.AddField(
            model_name='application',
            name='application_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
