# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_auto_20140810_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='Allday',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendar',
            name='End',
            field=models.CharField(null=True, max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendar',
            name='Start',
            field=models.CharField(null=True, max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendar',
            name='Title',
            field=models.CharField(max_length=100, default='My Event'),
            preserve_default=True,
        ),
    ]
