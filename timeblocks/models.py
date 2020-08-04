from django.db import models
from django.contrib.auth.models import User

class TimeBlockList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200, null=True)
    length = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class TimeBlock(models.Model):
    timeBlockList = models.ForeignKey(TimeBlockList, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True)
    length = models.IntegerField(null=True)


    def __str__(self):
        return self.name
