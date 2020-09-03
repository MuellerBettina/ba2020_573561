# Generated by Django 2.2.13 on 2020-09-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeblocks', '0007_timeblocklist_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeblocklist',
            name='color',
            field=models.CharField(choices=[('#fc5353', 'red'), ('#fcb34e', 'orange'), ('#ffcc00', 'yellow'), ('#76fc58', 'green'), ('#67b4fc', 'blue'), ('#b467fc', 'purple'), ('#ffffff', 'white')], default='white', max_length=7),
        ),
    ]
