# Generated by Django 3.0.2 on 2020-01-13 03:03

import attendees.persons.models.utility
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_attendee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('relation', models.CharField(db_index=True, max_length=32)),
                ('from_attendee', models.ForeignKey(on_delete=models.SET(0), related_name='from_attendee', to='persons.Attendee')),
                ('to_attendee', models.ForeignKey(on_delete=models.SET(0), related_name='to_attendee', to='persons.Attendee')),
            ],
            options={
                'db_table': 'persons_relationships',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
        migrations.AddField(
            model_name='attendee',
            name='relations',
            field=models.ManyToManyField(related_name='_attendee_relations_+', through='persons.Relationship', to='persons.Attendee'),
        ),
        migrations.AddConstraint(
            model_name='relationship',
            constraint=models.UniqueConstraint(fields=('from_attendee', 'to_attendee'), name='from_attendee_to_attendee'),
        ),
    ]