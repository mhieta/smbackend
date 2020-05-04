# Generated by Django 2.2.12 on 2020-05-04 06:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0074_update_unit_root_service_nodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='accessibility_viewpoints',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitaccessibilityshortcomings',
            name='accessibility_description',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='unitaccessibilityshortcomings',
            name='accessibility_shortcoming_count',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
    ]
