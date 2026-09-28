# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('magi', '0009_auto_20160929_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 29, 16, 51, 52, 717692), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='language',
            field=models.CharField(max_length=4, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('it', 'Italian'), ('fr', 'French'), ('de', 'German'), ('pl', 'Polish'), ('ja', 'Japanese')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='language',
            field=models.CharField(max_length=4, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('it', 'Italian'), ('fr', 'French'), ('de', 'German'), ('pl', 'Polish'), ('ja', 'Japanese')]),
            preserve_default=True,
        ),
    ]
