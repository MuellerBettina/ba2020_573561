# Generated by Django 2.2.13 on 2020-07-22 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0014_auto_20200722_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 19, 11, 2, 443103, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 19, 11, 2, 443084, tzinfo=utc)),
        ),
    ]
