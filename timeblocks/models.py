from django.core.validators import MaxValueValidator, MinValueValidator
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

class TimeBlockList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200, null=True)
    length = models.IntegerField(default=5, validators=[MaxValueValidator(60), MinValueValidator(1)])
    color = models.CharField(max_length=7, choices=COLORS, default="white")

    def __str__(self):
        return self.name


class TimeBlock(models.Model):
    timeBlockList = models.ForeignKey(TimeBlockList, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True)
    length = models.IntegerField(null=True)


    def __str__(self):
        return self.name
