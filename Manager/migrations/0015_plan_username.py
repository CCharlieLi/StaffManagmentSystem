# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0014_plan_planlevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='UserName',
            field=models.CharField(max_length=20, default=''),
            preserve_default=True,
        ),
    ]
