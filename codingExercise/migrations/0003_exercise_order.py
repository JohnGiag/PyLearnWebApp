# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codingExercise', '0002_exercise_test_imports'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
