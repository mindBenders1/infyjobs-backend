# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-14 13:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1024)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('opt1', models.CharField(max_length=255)),
                ('opt2', models.CharField(max_length=255)),
                ('opt3', models.CharField(max_length=255)),
                ('opt4', models.CharField(max_length=255)),
                ('ans', models.CharField(max_length=255)),
                ('subject_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assessment.AssessmentTest')),
            ],
        ),
    ]
