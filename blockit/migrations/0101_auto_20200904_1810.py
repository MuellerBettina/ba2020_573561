# Generated by Django 2.2.13 on 2020-09-04 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0100_auto_20200904_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 4, 16, 10, 25, 537490, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='action',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 4, 16, 10, 25, 537472, tzinfo=utc)),
        ),
    ]
