# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-13 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=255),
        ),
    ]
