# Generated by Django 2.2.13 on 2020-09-07 08:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0113_auto_20200907_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 8, 23, 35, 198155, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='action',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 8, 23, 35, 198137, tzinfo=utc)),
        ),
    ]
