# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20160623_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='other_properties',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]
