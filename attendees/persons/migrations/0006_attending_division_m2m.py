# Generated by Django 3.0.2 on 2020-01-21 05:53

import attendees.persons.models.utility
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whereabouts', '0008_room'),
        ('persons', '0005_attending'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendingDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('attending', models.ForeignKey(on_delete=models.SET(0), to='persons.Attending')),
                ('division', models.ForeignKey(on_delete=models.SET(0), to='whereabouts.Division')),
            ],
            options={
                'db_table': 'persons_attending_divisions',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
        migrations.AddField(
            model_name='attending',
            name='divisions',
            field=models.ManyToManyField(through='persons.AttendingDivision', to='whereabouts.Division', related_name="divisions"),
        ),
        migrations.AddConstraint(
            model_name='attendingdivision',
            constraint=models.UniqueConstraint(fields=('attending', 'division'), name='attending_division'),
        ),
    ]
