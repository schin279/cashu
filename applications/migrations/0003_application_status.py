# Generated by Django 5.0.4 on 2024-04-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_remove_application_id_application_application_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
