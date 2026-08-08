# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('modification', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(verbose_name='Message')),
                ('language', models.CharField(max_length=4, verbose_name='Language', choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zh-tw', 'Traditional Chinese')])),
                ('tags_string', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to='activities/', null=True, verbose_name='Image', blank=True)),
                ('_cache_last_update', models.DateTimeField(null=True)),
                ('_cache_owner_username', models.CharField(max_length=32, null=True)),
                ('_cache_owner_email', models.EmailField(max_length=75, blank=True)),
                ('_cache_owner_preferences_status', models.CharField(max_length=12, null=True, choices=[('THANKS', 'Thanks'), ('SUPPORTER', 'Player'), ('LOVER', 'Super Player'), ('AMBASSADOR', 'Extreme Player'), ('PRODUCER', 'Master Player'), ('DEVOTEE', 'Ultimate Player')])),
                ('_cache_owner_preferences_twitter', models.CharField(max_length=32, null=True, blank=True)),
                ('likes', models.ManyToManyField(related_name='liked_activities', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name='activities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.PositiveIntegerField(choices=[(0, '{} liked your activity: {}.'), (1, '{} just followed you.')])),
                ('message_data', models.TextField(null=True, blank=True)),
                ('url_data', models.TextField(null=True, blank=True)),
                ('email_sent', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='notifications/', blank=True)),
                ('owner', models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('modification', models.DateTimeField(auto_now=True)),
                ('reported_thing', models.CharField(max_length=300)),
                ('reported_thing_title', models.CharField(max_length=300)),
                ('reported_thing_id', models.PositiveIntegerField()),
                ('message', models.TextField(verbose_name='Message')),
                ('staff_message', models.TextField(null=True)),
                ('status', models.PositiveIntegerField(default=0, choices=[(0, 'Pending'), (1, 'Deleted'), (2, 'Edited'), (3, 'Ignored')])),
                ('saved_data', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='user_images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, verbose_name='Platform', choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('reddit', 'Reddit'), ('schoolidolu', 'School Idol Tomodachi'), ('line', 'LINE Messenger'), ('tumblr', 'Tumblr'), ('twitch', 'Twitch'), ('steam', 'Steam'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('github', 'GitHub')])),
                ('value', models.CharField(help_text='Write your username only, no URL.', max_length=64, verbose_name='Username/ID', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-_\\. ]*$', 'Only alphanumeric and - _ characters are allowed.')])),
                ('relevance', models.PositiveIntegerField(blank=True, null=True, verbose_name='How often do you tweet/stream/post about ?', choices=[(0, 'Never'), (1, 'Sometimes'), (2, 'Often'), (3, 'Every single day')])),
                ('owner', models.ForeignKey(related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=4, verbose_name='Language', choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zh-tw', 'Traditional Chinese')])),
                ('description', models.TextField(help_text='Write whatever you want. You can add formatting and links using Markdown.', null=True, verbose_name='Description', blank=True)),
                ('favorite_character1', models.CharField(max_length=200, null=True, verbose_name='1st Favorite Character')),
                ('favorite_character2', models.CharField(max_length=200, null=True, verbose_name='2nd Favorite Character')),
                ('favorite_character3', models.CharField(max_length=200, null=True, verbose_name='3rd Favorite Character')),
                ('color', models.CharField(max_length=100, null=True, verbose_name='Color', blank=True)),
                ('birthdate', models.DateField(null=True, verbose_name='Birthdate', blank=True)),
                ('location', models.CharField(help_text='The city you live in. It might take up to 24 hours to update your location on the map.', max_length=200, null=True, verbose_name='Location', blank=True)),
                ('location_changed', models.BooleanField(default=False)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('status', models.CharField(max_length=12, null=True, choices=[('THANKS', 'Thanks'), ('SUPPORTER', 'Player'), ('LOVER', 'Super Player'), ('AMBASSADOR', 'Extreme Player'), ('PRODUCER', 'Master Player'), ('DEVOTEE', 'Ultimate Player')])),
                ('donation_link', models.CharField(max_length=200, null=True, blank=True)),
                ('donation_link_title', models.CharField(max_length=100, null=True, blank=True)),
                ('email_notifications_turned_off_string', models.CharField(max_length=15, null=True)),
                ('unread_notifications', models.PositiveIntegerField(default=0)),
                ('_cache_twitter', models.CharField(max_length=32, null=True, blank=True)),
                ('following', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(related_name='preferences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'list of userpreferences',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='images',
            field=models.ManyToManyField(related_name='report', verbose_name='Images', to='magi.UserImage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='owner',
            field=models.ForeignKey(related_name='reports', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='staff',
            field=models.ForeignKey(related_name='staff_reports', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
