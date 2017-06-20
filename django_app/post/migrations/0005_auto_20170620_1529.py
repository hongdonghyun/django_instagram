# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='html_content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(to='post.Tag'),
        ),
    ]