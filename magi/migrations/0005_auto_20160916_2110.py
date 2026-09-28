# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magi', '0004_auto_20160809_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='language',
            field=models.CharField(max_length=4, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('fr', 'French')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlink',
            name='relevance',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='How often do you tweet/stream/post about IDOLM@STER Cinderella Girls Starlight Stage?', choices=[(0, 'Never'), (1, 'Sometimes'), (2, 'Often'), (3, 'Every single day')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlink',
            name='type',
            field=models.CharField(max_length=20, verbose_name='Platform', choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('reddit', 'Reddit'), ('schoolidolu', 'School Idol Tomodachi'), ('stardustrun', 'Stardust Run'), ('frgl', 'fr.gl'), ('line', 'LINE Messenger'), ('tumblr', 'Tumblr'), ('twitch', 'Twitch'), ('steam', 'Steam'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('github', 'GitHub')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='language',
            field=models.CharField(max_length=4, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('fr', 'French')]),
            preserve_default=True,
        ),
    ]
