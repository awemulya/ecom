# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_item_other_properties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherproperties',
            name='item',
        ),
        migrations.DeleteModel(
            name='OtherProperties',
        ),
    ]
