# Generated by Django 2.2.13 on 2020-09-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeblocks', '0011_auto_20200905_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeblocklist',
            name='color',
            field=models.CharField(choices=[('#fc5353', 'red'), ('#f7a902', 'orange'), ('#ffcc00', 'yellow'), ('#76fc58', 'green'), ('#67b4fc', 'blue'), ('#b467fc', 'purple'), ('#f9e2ae', 'beige')], default='white', max_length=7),
        ),
    ]
