# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 03:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_auto_20171009_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychic',
            name='char_id',
        ),
    ]
