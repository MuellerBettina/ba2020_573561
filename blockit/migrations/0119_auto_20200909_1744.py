# Generated by Django 2.2.13 on 2020-09-09 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0118_auto_20200907_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 9, 15, 44, 22, 682919, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='action',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 9, 15, 44, 22, 682903, tzinfo=utc)),
        ),
    ]