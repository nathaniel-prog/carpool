# Generated by Django 3.1.3 on 2022-01-11 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0005_auto_20220110_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='chauffeur',
            name='passager',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 16, 4, 26, 771811)),
        ),
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 16, 4, 26, 771811)),
        ),
    ]
