# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0027_auto_20141023_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='gender',
            new_name='Gender',
        ),
    ]
