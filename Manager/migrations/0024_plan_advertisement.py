# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0023_auto_20141020_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='Advertisement',
            field=models.TextField(blank=True, default=''),
            preserve_default=True,
        ),
    ]
