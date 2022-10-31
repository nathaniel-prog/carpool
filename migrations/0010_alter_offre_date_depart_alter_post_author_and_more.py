# Generated by Django 4.0 on 2022-08-14 15:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('carpool', '0009_alter_offre_body_alter_offre_date_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='date_depart',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 4, 49, 467619)),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 4, 49, 467619)),
        ),
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 4, 49, 467619)),
        ),
    ]
