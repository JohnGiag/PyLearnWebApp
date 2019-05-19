# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-25 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codingExercise', '0007_auto_20180125_1321'),
        ('quiz', '0002_auto_20180115_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codingExercise.Chapter'),
        ),
    ]
