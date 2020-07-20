from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, unique=True)
    length = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)



    def schedule_later(self):
        self.save()

    def __str__(self):
        return self.name

