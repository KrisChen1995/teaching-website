# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-05 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
    ]
