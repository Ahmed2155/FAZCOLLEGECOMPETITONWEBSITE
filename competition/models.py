from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Competition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ParticipantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)  # e.g., Primary 3, 4, 5

    def __str__(self):
        return self.user.username


class Submission(models.Model):
    participant = models.ForeignKey(ParticipantProfile, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    entry_file = models.FileField(upload_to='submissions/')  # for uploading answers
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant.user.username} - {self.competition.title}"



