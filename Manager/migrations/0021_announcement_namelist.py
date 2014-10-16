# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0020_auto_20141016_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='Namelist',
            field=models.TextField(blank=True, default=''),
            preserve_default=True,
        ),
    ]
