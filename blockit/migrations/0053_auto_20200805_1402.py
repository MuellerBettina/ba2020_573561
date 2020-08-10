# Generated by Django 2.2.13 on 2020-08-05 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0052_auto_20200805_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 12, 2, 32, 405696, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 12, 2, 32, 405678, tzinfo=utc)),
        ),
    ]