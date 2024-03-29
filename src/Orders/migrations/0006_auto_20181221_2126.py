# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-21 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_order_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('in progress', 'In Progress'), ('delivered', 'Delivered'), ('refunded', 'Refunded')], default='created', max_length=100),
        ),
    ]
