# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0013_auto_20140904_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='planlevel',
            field=models.CharField(default='person', max_length=20),
            preserve_default=True,
        ),
    ]
