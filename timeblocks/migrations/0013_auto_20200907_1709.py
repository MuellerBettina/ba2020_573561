# Generated by Django 2.2.13 on 2020-09-07 15:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeblocks', '0012_auto_20200905_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeblocklist',
            name='length',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)]),
        ),
    ]
