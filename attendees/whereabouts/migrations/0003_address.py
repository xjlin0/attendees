# Generated by Django 3.0.2 on 2020-01-13 05:54

import attendees.persons.models.utility
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whereabouts', '0002_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('display_name', models.CharField(blank=True, null=True, db_index=True, max_length=50, help_text='optional label')),
                ('email1', models.EmailField(blank=True, db_index=True, max_length=254, null=True)),
                ('email2', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone1', models.CharField(blank=True, db_index=True, max_length=15, null=True)),
                ('phone2', models.CharField(blank=True, max_length=15, null=True)),
                ('address_type', models.CharField(max_length=20, default='street', blank=True, null=True, help_text='mailing, remote or street address')),
                ('street1', models.CharField(blank=True, max_length=50, null=True)),
                ('street2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(max_length=50, blank=True, null=True)),
                ('state', models.CharField(default='CA', max_length=10, blank=True, null=True)),
                ('zip_code', models.CharField(max_length=10, null=True, blank=True)),
                ('url', models.URLField(blank=True, null=True, max_length=255)),
                ('fields', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text="please keep {} here even there's no data", null=True)),
            ],
            options={
                'db_table': 'whereabouts_addresses',
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
    ]
