# Generated by Django 3.0.2 on 2020-01-13 14:49

import attendees.persons.models.utility
from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whereabouts', '0003_address'),
        ('occasions', '0000_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start', models.DateTimeField(blank=True, help_text='optional', null=True)),
                ('finish', models.DateTimeField(blank=True, help_text='optional', null=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('category', models.CharField(default='normal', help_text='normal, no-display, etc', max_length=20, blank=False, null=False, db_index=True)),
                ('display_name', models.CharField(max_length=50)),
                ('display_order', models.SmallIntegerField(blank=False, default=0, null=False)),
                ('slug', models.SlugField(max_length=50, unique=True, help_text='format: Organization_name-Assembly_name')),
                ('need_age', models.BooleanField('Does registration need age info?', null=False, blank=False, default=False, help_text="Does the age info of the participants required?")),
                ('division', models.ForeignKey(on_delete=models.SET(0), to='whereabouts.Division')),
            ],
            options={
                'db_table': 'occasions_assemblies',
                'verbose_name_plural': 'Assemblies',
                'ordering': ('display_order',),
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
    ]
