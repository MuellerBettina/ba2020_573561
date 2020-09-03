from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime

class Action(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, unique=True)
    length = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField(default=timezone.now())

    @property
    def get_html_url(self):
        url = reverse('blockit:event_edit', args=(self.id,))
        return f'<a href="{url}">{self.name}</a>'

    def schedule_later(self):
        self.save()

    def __str__(self):
        return self.name


