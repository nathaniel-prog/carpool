# Generated by Django 3.1.3 on 2022-01-04 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0002_chauffeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 4, 19, 28, 58, 629197)),
        ),
    ]
