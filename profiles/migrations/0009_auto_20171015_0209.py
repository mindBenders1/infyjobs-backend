# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_userprofile_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='user_profile/profile_pic'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(null=True, upload_to='userprofile/cv'),
        ),
    ]
