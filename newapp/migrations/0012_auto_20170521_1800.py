# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-21 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import newapp.models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=newapp.models.upload_image),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=redactor.fields.RedactorField(),
        ),
    ]
