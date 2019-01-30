from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)


class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="none")
    birthdate = models.DateTimeField(default=now)
    platform =  models.TextField(max_length=300)

    def __str__(self):
        return self.firstname

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField(default=now)
