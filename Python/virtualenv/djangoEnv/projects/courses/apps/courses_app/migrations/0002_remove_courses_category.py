# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='category',
        ),
    ]