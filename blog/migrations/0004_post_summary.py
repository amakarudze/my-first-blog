# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 20:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(default=datetime.datetime(2016, 3, 18, 20, 17, 46, 703324, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]