# Generated by Django 2.2.13 on 2020-09-09 20:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockit', '0123_auto_20200909_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 9, 20, 36, 12, 758278, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='action',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 9, 20, 36, 12, 758260, tzinfo=utc)),
        ),
    ]