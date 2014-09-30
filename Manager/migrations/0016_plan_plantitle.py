# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0015_plan_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plantitle',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
