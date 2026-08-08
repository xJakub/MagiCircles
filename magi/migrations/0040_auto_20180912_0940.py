# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magi', '0039_auto_20180727_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=1500, verbose_name='Message')),
                ('seen', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(related_name='sent_messages', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
                ('to_user', models.ForeignKey(related_name='received_messages', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='i_private_message_settings',
            field=models.PositiveIntegerField(default=0, verbose_name='Who is allowed to send you private messages?', choices=[(0, 'Anyone'), (1, 'Only people I follow'), (2, 'Nobody')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='m_message',
            field=models.TextField(max_length=15000, verbose_name='Message'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prize',
            name='i_character',
            field=models.CharField(max_length=200, null=True, verbose_name='Character', choices=[('1', 'Kasumi Toyama'), ('2', 'an idol'), ('3', 'Kasumi Toyamaa'), ('4', 'Rimi Ushigome'), ('5', 'Saaya Yamabuki'), ('6', 'Arisa Ichigaya'), ('7', 'Tae Hanazono')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlink',
            name='i_type',
            field=models.CharField(max_length=20, verbose_name='Platform', choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('reddit', 'Reddit'), ('schoolidolu', 'School Idol Tomodachi'), ('cpro', 'Cinderella Producers'), ('bang', 'Bandori Party'), ('stardustrun', 'Stardust Run'), ('frgl', 'fr.gl'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tumblr', 'Tumblr'), ('twitch', 'Twitch'), ('steam', 'Steam'), ('osu', 'osu!'), ('pixiv', 'Pixiv'), ('deviantart', 'DeviantArt'), ('crunchyroll', 'Crunchyroll'), ('mal', 'MyAnimeList'), ('animeplanet', 'Anime-Planet'), ('myfigurecollection', 'MyFigureCollection'), ('line', 'LINE Messenger'), ('github', 'GitHub'), ('carrd', 'Carrd'), ('listography', 'Listography')]),
            preserve_default=True,
        ),
    ]
