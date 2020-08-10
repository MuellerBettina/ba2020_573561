from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=False)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    @classmethod
    def create(cls, title, user, start_time, end_time):
        event = cls(title=title, user=user, start_time=start_time, end_time=end_time)

        return event
