# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_auto_20150203_2219'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='PeopleType',
        ),
    ]
