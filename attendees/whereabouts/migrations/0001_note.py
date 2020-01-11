# Generated by Django 3.0.2 on 2020-01-11 23:34

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('whereabouts', '0000_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('object_id', models.BigIntegerField()),
                ('note_type', models.CharField(blank=True, max_length=20, null=True)),
                ('note_text', models.TextField()),
                ('content_type', models.ForeignKey(on_delete=models.SET(0), to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'whereabouts_notes',
                'ordering': ('-modified',),
            },
        ),
    ]
