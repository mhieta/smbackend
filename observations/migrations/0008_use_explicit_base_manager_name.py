# Generated by Django 2.2.12 on 2020-04-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0007_protect_historical_observations_on_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoricalobservation',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='descriptiveobservation',
            options={'base_manager_name': 'objects'},
        ),
    ]