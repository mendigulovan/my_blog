# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.Post'),
        ),
    ]