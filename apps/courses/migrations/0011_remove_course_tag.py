# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-07 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20190405_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='tag',
        ),
    ]