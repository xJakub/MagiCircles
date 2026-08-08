# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magi', '0014_auto_20161011_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='language',
            field=models.CharField(max_length=4, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('it', 'Italian'), ('fr', 'French'), ('de', 'German'), ('pl', 'Polish'), ('ja', 'Japanese'), ('zh-hans', 'Simplified Chinese'), ('pt-br', 'Brazilian Portuguese')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='language',
            field=models.CharField(max_length=4, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('it', 'Italian'), ('fr', 'French'), ('de', 'German'), ('pl', 'Polish'), ('ja', 'Japanese'), ('zh-hans', 'Simplified Chinese'), ('pt-br', 'Brazilian Portuguese')]),
            preserve_default=True,
        ),
    ]
