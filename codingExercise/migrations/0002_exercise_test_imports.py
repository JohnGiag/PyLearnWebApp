# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codingExercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='test_imports',
            field=models.TextField(blank=True),
        ),
    ]