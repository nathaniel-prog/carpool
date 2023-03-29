# Generated by Django 4.0 on 2023-03-12 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0017_remove_offre_adresse_alter_offre_date_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='date_depart',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 16, 53, 19, 916077), null=True),
        ),
        migrations.AlterField(
            model_name='offre',
            name='depart',
            field=models.CharField(default='Netanya', max_length=150, null=True, verbose_name='indiquez votre ville et adresse de depart ou un lieu'),
        ),
        migrations.AlterField(
            model_name='offre',
            name='ville',
            field=models.CharField(default='Netanya', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 16, 53, 19, 916077)),
        ),
        migrations.AlterField(
            model_name='post',
            name='depart',
            field=models.CharField(default='Netanya', max_length=150, null=True, verbose_name='indiquez votre adresse de depart'),
        ),
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 16, 53, 19, 916077)),
        ),
        migrations.AlterField(
            model_name='post',
            name='ville',
            field=models.CharField(default='Netanya', max_length=150),
        ),
    ]
