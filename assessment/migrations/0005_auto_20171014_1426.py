# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-14 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0004_auto_20171014_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.AssessmentTest'),
        ),
    ]