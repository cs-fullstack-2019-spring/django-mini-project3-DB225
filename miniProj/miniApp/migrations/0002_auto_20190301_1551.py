# Generated by Django 2.0.6 on 2019-03-01 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miniApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecardmodel',
            name='date_of_work',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='timecardmodel',
            name='hours',
            field=models.IntegerField(),
        ),
    ]
