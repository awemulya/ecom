from __future__ import unicode_literals

from django.db import migrations, models


def add_pieces_unit(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
     # version than this migration expects. We use the historical version.
     Unit = apps.get_model("inventory", "Unit")
     Unit.objects.get_or_create(name='Pieces', short_name='pcs')


class Migration(migrations.Migration):
    pass
    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_pieces_unit),
    ]

