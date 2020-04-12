# Generated by Django 3.0.2 on 2020-04-11 15:33

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whereabouts', '0009_attendee_address_m2m'),
        ('occasions', '0009_meet_attending'),
        ('users', '0002_user_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('category', models.CharField(default='main', help_text="Type of menu, such as 'main', 'side', etc", max_length=32)),
                ('urn', models.CharField(blank=True, help_text="relative path (including leading & ending slash '/') such as /0_organization_name/app/division/meets/", max_length=255, null=True)),
                ('display_name', models.CharField(help_text="description of the path, such as 'Character index page'", max_length=50)),
                ('display_order', models.SmallIntegerField(default=0)),
                ('infos', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text="HTML attributes & more such as {'class': 'dropdown-item'}. Please keep {} here even no data", null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('organization', models.ForeignKey(default=0, help_text='Organization of the menu', on_delete=models.SET(0), to='whereabouts.Organization')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=models.SET(-1), related_name='children', to='users.Menu')),
            ],
            options={
                'db_table': 'users_menus',
            },
        ),
        migrations.AddConstraint(
            model_name='menu',
            constraint=models.UniqueConstraint(fields=('organization', 'category', 'urn'), name='organization_category_urn'),
        ),
    ]