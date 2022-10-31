# Generated by Django 4.0 on 2022-10-20 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0014_alter_offre_body_alter_offre_date_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='arrive',
            field=models.CharField(default='tel-aviv', max_length=150, verbose_name='indiquez votre adresse de depart ou un lieu '),
        ),
        migrations.AlterField(
            model_name='offre',
            name='body',
            field=models.CharField(max_length=255, null=True, verbose_name='y a til des remarques a faire?'),
        ),
        migrations.AlterField(
            model_name='offre',
            name='date_depart',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 20, 12, 37, 9, 481399), null=True),
        ),
        migrations.AlterField(
            model_name='offre',
            name='depart',
            field=models.CharField(default='Milan', max_length=150, null=True, verbose_name='indiquez votre adresse de depart ou un lieu'),
        ),
        migrations.AlterField(
            model_name='offre',
            name='ville',
            field=models.CharField(default='Milan', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 20, 12, 37, 9, 481399)),
        ),
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 20, 12, 37, 9, 481399)),
        ),
    ]