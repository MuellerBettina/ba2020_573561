from django.conf import settings
from django.db import models
from django.utils import timezone

class Element(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def schedule_later(self):
        self.save()

    def __str__(self):
        return self.name

