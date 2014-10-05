# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0009_auto_20140903_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='Score',
            field=models.CharField(max_length=5, blank=True, null=True, default='0'),
        ),
    ]
