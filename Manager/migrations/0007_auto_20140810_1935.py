# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0006_auto_20140810_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='userID',
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
    ]
