# Generated by Django 2.2.13 on 2020-07-30 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0023_auto_20200730_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 15, 13, 52, 42196, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 15, 13, 52, 42178, tzinfo=utc)),
        ),
    ]
