# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-13 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codingExercise', '0007_auto_20180125_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='next',
        ),
    ]
