# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0016_plan_plantitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='Datetime',
            field=models.CharField(max_length=20),
        ),
    ]
