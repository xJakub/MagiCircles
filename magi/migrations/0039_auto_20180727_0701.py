# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magi', '0038_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='description',
            new_name='m_description',
        ),
        migrations.AddField(
            model_name='activity',
            name='archived_by_owner',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='archived_by_staff',
            field=models.ForeignKey(related_name='archived_activities', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='reported_thing_owner_id',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='_cache_description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='i_activities_language',
            field=models.CharField(default='en', max_length=10, verbose_name='Post activities in {language}'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='i_default_activities_tab',
            field=models.PositiveIntegerField(default=0, verbose_name='Default tab'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='last_bump_counter',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='last_bump_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='last_bump',
            field=models.DateTimeField(null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='i_message',
            field=models.PositiveIntegerField(verbose_name='Notification type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prize',
            name='i_character',
            field=models.CharField(max_length=200, null=True, verbose_name='Character', choices=[('1', 'Kasumi Toyama'), ('2', 'an idol')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlink',
            name='i_type',
            field=models.CharField(max_length=20, verbose_name='Platform', choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('reddit', 'Reddit'), ('schoolidolu', 'School Idol Tomodachi'), ('cpro', 'Cinderella Producers'), ('bang', 'Bandori Party'), ('stardustrun', 'Stardust Run'), ('frgl', 'fr.gl'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tumblr', 'Tumblr'), ('twitch', 'Twitch'), ('steam', 'Steam'), ('osu', 'Osu'), ('pixiv', 'Pixiv'), ('deviantart', 'DeviantArt'), ('crunchyroll', 'Crunchyroll'), ('mal', 'MyAnimeList'), ('animeplanet', 'Anime-Planet'), ('myfigurecollection', 'MyFigureCollection'), ('line', 'LINE Messenger'), ('github', 'GitHub'), ('carrd', 'Carrd'), ('listography', 'Listography')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='donation_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Custom link', validators=[django.core.validators.URLValidator()]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='donation_link_title',
            field=models.CharField(max_length=100, null=True, verbose_name='Title', blank=True),
            preserve_default=True,
        ),
    ]
