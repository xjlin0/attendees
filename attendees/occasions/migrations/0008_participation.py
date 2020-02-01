# Generated by Django 3.0.2 on 2020-02-01 14:57

import attendees.persons.models.utility
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_attending_address'),
        ('occasions', '0007_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('is_removed', models.BooleanField(default=False)),
                ('free', models.IntegerField(blank=True, default=0, help_text='multitasking: the person cannot join other sessions if negative', null=True)),
                ('attending', models.ForeignKey(on_delete=models.SET(0), to='persons.Attending')),
                ('character', models.ForeignKey(on_delete=models.SET(0), to='occasions.Character')),
                ('session', models.ForeignKey(on_delete=models.SET(0), to='occasions.Session')),
                ('team', models.ForeignKey(blank=True, default=None, help_text='empty for main group', null=True, on_delete=django.db.models.deletion.SET_NULL, to='occasions.Team')),
            ],
            options={
                'db_table': 'occasions_participations',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
            managers=[
                ('timeframed', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='attendings',
            field=models.ManyToManyField(through='occasions.Participation', to='persons.Attending'),
        ),
    ]
