# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170612_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
