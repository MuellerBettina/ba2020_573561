# Generated by Django 2.2.13 on 2020-09-04 17:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0102_auto_20200904_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 4, 17, 58, 55, 371464, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='action',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 4, 17, 58, 55, 371446, tzinfo=utc)),
        ),
    ]
