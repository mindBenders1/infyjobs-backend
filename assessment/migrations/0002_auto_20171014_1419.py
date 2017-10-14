# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-14 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmenttest',
            name='subject',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.RemoveField(
            model_name='question',
            name='subject_details',
        ),
        migrations.AddField(
            model_name='question',
            name='subject_details',
            field=models.ManyToManyField(to='assessment.AssessmentTest'),
        ),
    ]
