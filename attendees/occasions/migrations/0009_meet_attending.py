# Generated by Django 3.0.2 on 2020-01-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasions', '0008_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='attendings',
            field=models.ManyToManyField(related_name='attendings', through='persons.AttendingMeet', to='persons.Attending'),
        ),
    ]
