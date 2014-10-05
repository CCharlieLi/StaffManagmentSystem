# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0010_auto_20140903_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Score',
            field=models.CharField(blank=True, default='0', null=True, max_length=5),
        ),
    ]
