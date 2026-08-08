# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0006_translatednames_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gacha',
            name='i_attribute',
            field=models.PositiveIntegerField(default=0, choices=[(0, 'smile'), (1, 'pure'), (2, 'cool')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gacha',
            name='i_power',
            field=models.PositiveIntegerField(default=0, choices=[(0, 'Happy'), (1, 'Cool'), (2, 'Rock')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gacha',
            name='i_rarity',
            field=models.PositiveIntegerField(default=0, choices=[(0, 'N'), (1, 'R'), (2, 'SR')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gacha',
            name='i_super_power',
            field=models.PositiveIntegerField(default=0, choices=[(0, 'Happy'), (1, 'Cool'), (2, 'Rock')]),
            preserve_default=True,
        ),
    ]
