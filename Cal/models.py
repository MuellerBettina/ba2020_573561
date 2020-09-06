from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


COLORS = [
    ('#fc5353', 'red'),
    ('#f7a902', 'orange'),
    ('#ffcc00', 'yellow'),
    ('#76fc58', 'green'),
    ('#67b4fc', 'blue'),
    ('#b467fc', 'purple'),
    ('#f9e2ae', 'beige'),
]

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=False)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    the_start_time = models.TimeField(null=True)
    the_end_time = models.TimeField(null=True)
    the_date = models.DateField(null=True)
    color = models.CharField(max_length=7, choices=COLORS, default="white")

    def __str__(self):
        return self.title + " " + str(self.the_start_time) + "-" + str(self.the_end_time)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    @classmethod
    def create(cls, title, user, start_time, end_time, the_date, the_start_time, the_end_time, color):
        event = cls(title=title, user=user, start_time=start_time, end_time=end_time, the_date=the_date,
                    the_start_time=the_start_time, the_end_time=the_end_time, color=color)

        return event


