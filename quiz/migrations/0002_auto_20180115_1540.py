# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['order'], 'verbose_name': 'Quiz', 'verbose_name_plural': 'Quizes'},
        ),
        migrations.AddField(
            model_name='quiz',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
