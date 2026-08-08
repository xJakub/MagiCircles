# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magi', '0016_auto_20161101_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='language',
            field=models.CharField(max_length=10, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('it', 'Italian'), ('fr', 'French'), ('de', 'German'), ('pl', 'Polish'), ('ja', 'Japanese'), ('kr', 'Korean'), ('zh-hans', 'Simplified Chinese'), ('pt-br', 'Brazilian Portuguese')]),
            preserve_default=True,
        ),
    ]
