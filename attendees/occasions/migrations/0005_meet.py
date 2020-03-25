# Generated by Django 3.0.2 on 2020-01-14 06:10

import attendees.persons.models.utility
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whereabouts', '0004_assembly_address_m2m'),
        ('occasions', '0004_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start', models.DateTimeField(blank=True, null=True, help_text='optional')),
                ('finish', models.DateTimeField(blank=True, null=True, help_text='optional')),
                ('is_removed', models.BooleanField(default=False)),
                ('display_name', models.CharField(blank=True, null=True, db_index=True, help_text='The Rock, Little Foot, singspiration, A/V control, etc.', max_length=50)),
                ('slug', models.SlugField(max_length=50, unique=True)),
                ('info', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, null=True, max_length=255)),
                ('site_type', models.ForeignKey(help_text='location: django_content_type id for table name', on_delete=models.SET(0), to='contenttypes.ContentType')),
                ('site_id', models.BigIntegerField()),
                ('assembly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='occasions.Assembly')),
            ],
            options={
                'db_table': 'occasions_meets',
            },
            bases=(models.Model, attendees.persons.models.utility.Utility),
        ),
    ]
