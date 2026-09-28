# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import magi.utils


class Migration(migrations.Migration):

    dependencies = [
        ('magi', '0050_report_is_suggestededit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='_original_image',
            field=models.ImageField(max_length=255, null=True, upload_to=magi.utils.uploadTiny('activities')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(upload_to=magi.utils.uploadToRandom('activities'), max_length=255, blank=True, help_text='Only post official artworks, artworks you own, or fan artworks that are approved by the artist and credited.', null=True, verbose_name='Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='badge',
            name='image',
            field=models.ImageField(upload_to=magi.utils.uploadItem('badges'), max_length=255, verbose_name='Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donationmonth',
            name='image',
            field=models.ImageField(upload_to=magi.utils.uploadItem('badges'), max_length=255, verbose_name='Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prize',
            name='image',
            field=models.ImageField(upload_to=magi.utils.uploadItem('prize'), max_length=255, verbose_name='Prize image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prize',
            name='image2',
            field=models.ImageField(max_length=255, upload_to=magi.utils.uploadItem('prize'), null=True, verbose_name='2nd image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prize',
            name='image3',
            field=models.ImageField(max_length=255, upload_to=magi.utils.uploadItem('prize'), null=True, verbose_name='3rd image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prize',
            name='image4',
            field=models.ImageField(max_length=255, upload_to=magi.utils.uploadItem('prize'), null=True, verbose_name='4th image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='image',
            field=models.ImageField(upload_to=magi.utils.uploadToRandom('staff_photos'), max_length=255, blank=True, help_text="Photograph of yourself. Real life photos look friendlier when we introduce the team. If you really don't want to show your face, you can use an avatar, but we prefer photos :)", null=True, verbose_name='Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userimage',
            name='_thumbnail_image',
            field=models.ImageField(max_length=255, null=True, upload_to=magi.utils.uploadThumb('user_images')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(max_length=255, upload_to=magi.utils.uploadToRandom('user_images')),
            preserve_default=True,
        ),
    ]
