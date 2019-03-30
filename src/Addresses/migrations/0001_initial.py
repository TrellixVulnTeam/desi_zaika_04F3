# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-16 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=150)),
                ('address_line_2', models.CharField(blank=True, max_length=150, null=True)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.UserBillingProfile')),
            ],
        ),
    ]
