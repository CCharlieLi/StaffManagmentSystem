# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0010_auto_20150205_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=b'website/images', verbose_name=b'Image(700x240)'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to=b'website/file'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=b'website/images', verbose_name=b'Image(700x240)'),
        ),
        migrations.AlterField(
            model_name='partnership',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=b'website/images', verbose_name=b'Image(700x240)'),
        ),
        migrations.AlterField(
            model_name='people',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=b'website/images', verbose_name=b'Image(220x220/220x140)'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to=b'website/file'),
        ),
    ]
