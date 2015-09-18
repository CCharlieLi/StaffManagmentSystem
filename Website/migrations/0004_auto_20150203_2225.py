# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_auto_20150203_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partnership',
            old_name='Type',
            new_name='PeopleType',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Type',
            new_name='PeopleType',
        ),
    ]
