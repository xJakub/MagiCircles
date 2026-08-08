# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import magi.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magi', '0037_auto_20180605_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Prize name')),
                ('image', models.ImageField(upload_to=magi.utils.uploadItem('prize/'), verbose_name='Prize image')),
                ('image2', models.ImageField(upload_to=magi.utils.uploadItem('prize/'), null=True, verbose_name='2nd image')),
                ('image3', models.ImageField(upload_to=magi.utils.uploadItem('prize/'), null=True, verbose_name='3rd image')),
                ('image4', models.ImageField(upload_to=magi.utils.uploadItem('prize/'), null=True, verbose_name='4th image')),
                ('value', models.DecimalField(help_text='in USD', null=True, verbose_name='Value', max_digits=6, decimal_places=2)),
                ('i_character', models.CharField(max_length=200, null=True, verbose_name='Character', choices=[('1', 'qwert'), ('2', 'an idol')])),
                ('m_details', models.TextField(null=True, verbose_name='Details')),
                ('giveaway_url', models.CharField(help_text='If you specify a giveaway URL, the prize will be considered unavailable for future giveaways', max_length=100, null=True, verbose_name='Giveaway URL')),
                ('owner', models.ForeignKey(related_name='added_prizes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
