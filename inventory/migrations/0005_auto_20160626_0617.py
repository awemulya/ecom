# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20160623_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ne',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='name_ne',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
