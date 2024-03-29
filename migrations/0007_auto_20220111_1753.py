# Generated by Django 3.1.3 on 2022-01-11 15:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carpool', '0006_auto_20220111_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 17, 53, 23, 868449)),
        ),
        migrations.AlterField(
            model_name='post',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 17, 53, 23, 868449)),
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(default='', max_length=150, null=True, verbose_name='indiquez votre adresse de depart')),
                ('arrive', models.CharField(default='', max_length=150, null=True)),
                ('adresse', models.CharField(max_length=150)),
                ('passagers', models.PositiveIntegerField(verbose_name='indiquez le nombre de personnes ')),
                ('num_phone', phonenumber_field.modelfields.PhoneNumberField(default='+972', max_length=128, null=True, region=None)),
                ('date_depart', models.DateTimeField(default=datetime.datetime(2022, 1, 11, 17, 53, 23, 868449))),
                ('body', models.CharField(max_length=255, null=True, verbose_name='indiquez l heure du depart')),
                ('exp_date', models.DateTimeField(default=datetime.datetime(2022, 1, 11, 17, 53, 23, 868449))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
