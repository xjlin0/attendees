# Generated by Django 3.0.2 on 2020-02-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whereabouts', '0001_organization'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, blank=True, default=None, help_text='Primary organization of the user', on_delete=models.SET_NULL, to='whereabouts.Organization'),
        ),
    ]