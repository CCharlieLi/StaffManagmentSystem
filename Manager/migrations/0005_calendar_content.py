# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_auto_20140810_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='Content',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
