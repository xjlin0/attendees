# Generated by Django 3.0.2 on 2020-01-21 05:33

import attendees.persons.models.utility
from django.db import migrations, models
from django.contrib.postgres.fields.jsonb import JSONField
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=20, null=False, blank=False, default="normal", help_text="normal, not_going, coworker, etc")),
                ('attendee', models.ForeignKey(null=False, blank=False, on_delete=models.SET(0), to='persons.Attendee', related_name="attendings")),
                ('registration', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='persons.Registration')),
                ('start', models.DateTimeField(blank=False, null=False, db_index=True, default=attendees.persons.models.utility.Utility.now_with_timezone)),
                ('finish', models.DateTimeField(blank=False, null=False, db_index=True, help_text="Required for user to filter by time")),
                ('infos', JSONField(blank=True, default=dict, help_text='Example: {"grade": 5, "age": 11, "bed_needs": 1, "mobility": 300}. Please keep {} here even no data', null=True)),
            ],
            options={
                'db_table': 'persons_attendings',
                'ordering': ['registration'],
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
        migrations.AddIndex(
            model_name='attending',
            index=django.contrib.postgres.indexes.GinIndex(fields=['infos'], name='attending_infos_gin'),
        ),
    ]
