# Generated by Django 2.2.13 on 2020-07-22 11:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0007_auto_20200721_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 11, 11, 17, 982511, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 11, 11, 17, 982494, tzinfo=utc)),
        ),
    ]
