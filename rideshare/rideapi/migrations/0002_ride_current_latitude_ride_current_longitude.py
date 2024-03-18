# Generated by Django 5.0.3 on 2024-03-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='current_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='current_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
