# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('level', models.PositiveIntegerField(null=True, verbose_name='Level')),
                ('owner', models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CCSVTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_data', models.TextField(null=True, blank=True)),
                ('c_abilities', models.TextField(null=True, blank=True)),
                ('c_tags', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IChoicesTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_attribute', models.PositiveIntegerField(default=0, choices=[(0, 'smile'), (1, 'pure'), (2, 'cool')])),
                ('i_power', models.PositiveIntegerField(default=0, choices=[(0, 'Happy'), (1, 'Cool'), (2, 'Rock')])),
                ('i_super_power', models.PositiveIntegerField(default=0, choices=[(0, 'Happy'), (1, 'Cool'), (2, 'Rock')])),
                ('i_rarity', models.PositiveIntegerField(default=0, choices=[(0, 'N'), (1, 'R'), (2, 'SR')])),
                ('i_language', models.CharField(default='en', max_length=10, verbose_name='Language', choices=[('en', 'English'), ('es', 'Spanish'), ('ru', 'Russian'), ('it', 'Italian')])),
                ('i_notification', models.PositiveIntegerField(default=0, verbose_name='Notification type', choices=[(0, 'When someone likes your activity.'), (1, 'When someone follows you.')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
