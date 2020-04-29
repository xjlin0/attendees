# Generated by Django 3.0.2 on 2020-02-01 14:57

import attendees.persons.models.utility
from django.db import migrations, models
from django.contrib.postgres.fields.jsonb import JSONField
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0010_attendee_address'),
        ('occasions', '0007_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start', models.DateTimeField(blank=True, null=True, help_text='optional')),
                ('finish', models.DateTimeField(blank=True, null=True, help_text='optional')),
                ('is_removed', models.BooleanField(default=False)),
                ('free', models.SmallIntegerField(blank=True, default=0, help_text='multitasking: the person cannot join other gatherings if negative', null=True)),
                ('attending', models.ForeignKey(on_delete=models.SET(0), to='persons.Attending')),
                ('character', models.ForeignKey(on_delete=models.SET(0), to='occasions.Character')),
                ('gathering', models.ForeignKey(on_delete=models.SET(0), to='occasions.Gathering')),
                ('team', models.ForeignKey(blank=True, default=None, help_text='empty for main meet', null=True, on_delete=django.db.models.deletion.SET_NULL, to='occasions.Team')),
                ('category', models.CharField(max_length=20, null=False, blank=False, default="scheduled", db_index=True, help_text="RSVPed, leave, remote, etc")),
                ('display_order', models.SmallIntegerField(blank=False, default=0, null=False)),
                ('infos', JSONField(blank=True, default=dict, help_text='Example: {"kid_points": 5}. Please keep {} here even no data', null=True)),
            ],
            options={
                'db_table': 'occasions_attendances',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
        migrations.AddField(
            model_name='gathering',
            name='attendings',
            field=models.ManyToManyField(through='occasions.Attendance', to='persons.Attending'),
        ),
    ]
