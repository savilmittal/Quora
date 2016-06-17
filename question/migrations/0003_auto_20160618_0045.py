# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-17 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20160617_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='upvoted_by',
            field=models.ManyToManyField(null=True, related_name='questions_upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]