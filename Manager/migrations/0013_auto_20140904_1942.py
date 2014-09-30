# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0012_auto_20140904_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['id']},
        ),
    ]
