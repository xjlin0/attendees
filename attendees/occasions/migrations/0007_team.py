# Generated by Django 3.0.2 on 2020-01-21 06:13

import attendees.persons.models.utility
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('occasions', '0006_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('key', models.CharField(max_length=50, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=50, null=True)),
                ('display_order', models.IntegerField(blank=True, default=0, null=True)),
                ('group', models.ForeignKey(on_delete=models.SET(0), to='occasions.Group')),
            ],
            options={
                'db_table': 'occasions_teams',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
    ]
