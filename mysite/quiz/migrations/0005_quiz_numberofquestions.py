# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20170506_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='numberOfQuestions',
            field=models.IntegerField(default='1'),
        ),
    ]
