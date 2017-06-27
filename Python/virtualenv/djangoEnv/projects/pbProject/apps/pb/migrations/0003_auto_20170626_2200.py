# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pb', '0002_auto_20170626_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poke',
            name='pokee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gotPoked', to='login_registration.User'),
        ),
        migrations.AlterField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='login_registration.User'),
        ),
    ]
