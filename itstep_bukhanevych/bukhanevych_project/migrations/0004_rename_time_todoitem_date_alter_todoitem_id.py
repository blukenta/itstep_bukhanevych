# Generated by Django 5.0.6 on 2024-06-01 16:31

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bukhanevych_project', '0003_alter_todoitem_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='time',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(blank=True, editable=False, primary_key=True, serialize=False),
        ),
    ]