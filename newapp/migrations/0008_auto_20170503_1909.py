# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20170503_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
