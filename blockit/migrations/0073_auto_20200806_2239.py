# Generated by Django 2.2.13 on 2020-08-06 20:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0072_auto_20200806_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 20, 39, 54, 618910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 20, 39, 54, 618892, tzinfo=utc)),
        ),
    ]
