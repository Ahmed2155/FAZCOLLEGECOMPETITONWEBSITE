# Generated by Django 5.2.1 on 2025-06-02 22:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='participantprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='participant',
        ),
        migrations.CreateModel(
            name='CompetitionRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('grade_level', models.CharField(max_length=50)),
                ('school_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=50)),
                ('has_written_cbt', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=11)),
                ('competition_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
        migrations.DeleteModel(
            name='ParticipantProfile',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
    ]
