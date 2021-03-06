# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-16 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='num_of_completed_exercises',
            new_name='num_of_copmleted_exercises',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='num_of_completed_quizes',
            new_name='num_of_copmleted_quizes',
        ),
        migrations.AddField(
            model_name='completedexercise',
            name='answer',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='completedquiz',
            name='score',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
