# Generated by Django 3.0.2 on 2020-01-13 05:14

import attendees.persons.models.utility
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('whereabouts', '0000_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('key', models.CharField(help_text='alphanumeric only', max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'whereabouts_organizations',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
    ]
