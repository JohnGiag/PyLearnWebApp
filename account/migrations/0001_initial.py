# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 10:01
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(blank=True, max_length=50, null=True)),
                ('score', models.CharField(max_length=10)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Completed Quiz',
                'verbose_name_plural': 'Completed Quizes',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('totalQuizScore', models.FloatField(default=0)),
                ('quizAvgScore', models.FloatField(default=0)),
                ('num_of_completed_exercises', models.IntegerField(default=0)),
                ('num_of_completed_quizes', models.IntegerField(default=0)),
                ('num_of_achievements', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='completedquiz',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
        migrations.AddField(
            model_name='completedexercise',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
    ]
