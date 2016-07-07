# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-07 19:11
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='token',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='contact',
            field=models.BigIntegerField(validators=[django.core.validators.RegexValidator(code='nomatch', message='Please enter a valid contact', regex='^.{10}$')]),
        ),
    ]
