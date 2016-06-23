# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_auto_20160614_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('account_no', models.PositiveIntegerField()),
                ('current_balance', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterModelManagers(
            name='category',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='itemimages',
            name='file',
            field=models.ImageField(upload_to='items'),
        ),
        migrations.AddField(
            model_name='item',
            name='account',
            field=models.OneToOneField(null=True, related_name='item', to='inventory.InventoryAccount'),
        ),
    ]
