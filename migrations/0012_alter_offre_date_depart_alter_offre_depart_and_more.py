# Generated by Django 4.0 on 2022-10-18 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0011_offre_ville_post_ville_alter_offre_date_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='date_depart',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 5, 17, 288872)),
        ),
        migrations.AlterField(
            model_name='offre',
            name='depart',
            field=models.CharField(default='Tel Aviv', max_length=150, null=True, verbose_name='indiquez votre adresse de depart'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 5, 17, 288872)),
        ),
        migrations.AlterField(
            model_name='post',
            name='depart',
            field=models.CharField(default='Tel Aviv', max_length=150, null=True, verbose_name='indiquez votre adresse de depart'),
        ),
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 15, 5, 17, 288872)),
        ),
    ]
