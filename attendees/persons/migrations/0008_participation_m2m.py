# Generated by Django 3.0.2 on 2020-02-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasions', '0008_participation'),
        ('persons', '0007_attending_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='attending',
            name='sessions',
            field=models.ManyToManyField(through='occasions.Participation', to='occasions.Session'),
        ),
    ]
