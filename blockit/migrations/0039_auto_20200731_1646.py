# Generated by Django 2.2.13 on 2020-07-31 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0038_auto_20200731_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 46, 35, 721992, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 46, 35, 721972, tzinfo=utc)),
        ),
    ]