# Generated by Django 2.2.13 on 2020-08-05 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0061_auto_20200805_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 17, 8, 45, 895334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 17, 8, 45, 895315, tzinfo=utc)),
        ),
    ]