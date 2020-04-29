# Generated by Django 3.0.2 on 2020-01-13 03:03

from attendees.persons.models.utility import Utility
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_relationship_default_m2m'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('relation', models.CharField(max_length=32, null=False, blank=False, default="relation", db_index=True, help_text="example: father - son, husband - wife, etc")),
                ('category', models.CharField(max_length=32, null=False, blank=False, default="relatives", db_index=True, help_text="relative/friend, notifier/caregiver, SMS_kid_class, emergency_contact, etc")),
                ('from_attendee', models.ForeignKey(on_delete=models.SET(0), related_name='from_attendee', to='persons.Attendee')),
                ('to_attendee', models.ForeignKey(on_delete=models.SET(0), related_name='to_attendee', to='persons.Attendee')),
                ('finish', models.DateTimeField(null=False, blank=False, default=Utility.forever, help_text='The relation will be ended at when')),
            ],
            options={
                'db_table': 'persons_relationships',
            },
            bases=(models.Model, Utility),
        ),
        migrations.AddField(
            model_name='attendee',
            name='related_ones',
            field=models.ManyToManyField(related_name='_attendee_relations_+', through='persons.Relationship', to='persons.Attendee'),
        ),
        migrations.AddConstraint(
            model_name='relationship',
            constraint=models.UniqueConstraint(fields=('from_attendee', 'to_attendee', 'category', 'relation'), name='attendee_category_relation'),
        ),
    ]
