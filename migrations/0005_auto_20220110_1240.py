# Generated by Django 3.1.3 on 2022-01-10 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0004_auto_20220106_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 12, 40, 19, 267568)),
        ),
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 12, 40, 19, 267568)),
        ),
    ]