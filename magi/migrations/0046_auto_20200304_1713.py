# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magi', '0045_auto_20200228_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlink',
            name='i_type',
            field=models.CharField(max_length=20, verbose_name='Platform', choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('reddit', 'Reddit'), ('idolstory', 'Idol Story'), ('starlight', 'Starlight Academy'), ('cpro', 'Cinderella Producers'), ('schoolidolu', 'School Idol Tomodachi'), ('stardustrun', 'Stardust Run'), ('frgl', 'fr.gl'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tumblr', 'Tumblr'), ('twitch', 'Twitch'), ('steam', 'Steam'), ('osu', 'osu!'), ('pixiv', 'Pixiv'), ('deviantart', 'DeviantArt'), ('crunchyroll', 'Crunchyroll'), ('mal', 'MyAnimeList'), ('animeplanet', 'Anime-Planet'), ('myfigurecollection', 'MyFigureCollection'), ('line', 'LINE Messenger'), ('github', 'GitHub'), ('carrd', 'Carrd'), ('listography', 'Listography')]),
            preserve_default=True,
        ),
    ]
