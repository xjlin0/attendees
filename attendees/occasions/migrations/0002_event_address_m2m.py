# Generated by Django 3.0.2 on 2020-01-14 02:05

import attendees.persons.models.utility
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whereabouts', '0003_address'),
        ('occasions', '0001_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('category', models.CharField(help_text='primary, backup, etc', max_length=20, null=True)),
                ('address', models.ForeignKey(on_delete=models.SET(0), to='whereabouts.Address')),
                ('event', models.ForeignKey(on_delete=models.SET(0), to='occasions.Event')),
            ],
            options={
                'db_table': 'occasions_event_addresses',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
        migrations.AddField(
            model_name='event',
            name='addresses',
            field=models.ManyToManyField(through='occasions.EventAddress', to='whereabouts.Address'),
        ),
        migrations.AddConstraint(
            model_name='eventaddress',
            constraint=models.UniqueConstraint(fields=('event', 'address'), name='event_address'),
        ),
    ]