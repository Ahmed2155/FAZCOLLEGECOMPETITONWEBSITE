from django.db import models
from django.contrib.auth.models import User

class CompetitionRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Student Info
    student_name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    religion = models.CharField(max_length=50)
    has_written_cbt = models.BooleanField(default=False)

    # Parent/Teacher Info
    parent_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    # Competition
    competition_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.student_name}"


class Competition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ParticipantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    selected_competition_date = models.DateField()

    def __str__(self):
        return self.user.username

class Submission(models.Model):
    participant = models.ForeignKey(ParticipantProfile, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    entry_file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant.user.username} - {self.competition.title}"
