# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-16 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0002_example_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='example',
            options={'ordering': ['title']},
        ),
    ]
